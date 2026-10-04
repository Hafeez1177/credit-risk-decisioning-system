import pandas as pd
from pathlib import Path
import sqlite3

ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/"data/inventory_demand_3600.csv"
DB=ROOT/"reports/inventory.db"

def run():
    df=pd.read_csv(INPUT)
    required=["SKU","Week","Category","Region","Channel","Demand Units","On Hand Units","Inbound Units","Lead Time Days","Safety Stock Units","Promotion","Stockout","Revenue EUR"]
    missing=[c for c in required if c not in df.columns]
    if missing: raise ValueError(f"Missing columns: {missing}")
    if df[["SKU","Week"]].duplicated().any(): raise ValueError("Duplicate SKU-week rows")
    for c in ["Demand Units","On Hand Units","Inbound Units","Lead Time Days","Safety Stock Units"]:
        df[c]=pd.to_numeric(df[c],errors="raise")
        if (df[c]<0).any(): raise ValueError(f"Negative values in {c}")
    df["Week"]=pd.to_datetime(df["Week"],errors="raise")
    df["Available After Inbound"]=df["On Hand Units"]+df["Inbound Units"]
    df["Projected Gap"]=df["Demand Units"]+df["Safety Stock Units"]-df["Available After Inbound"]
    df["Reorder Flag"]=df["Projected Gap"]>0
    con=sqlite3.connect(DB)
    df.to_sql("inventory_demand",con,if_exists="replace",index=False)
    con.close()
    print(f"Processed {len(df):,} SKU-week observations.")

if __name__=="__main__":
    run()
