import pandas as pd
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/"data/inventory_demand_3600.csv")
assert len(df)==3600
assert not df[["SKU","Week"]].duplicated().any()
assert df.isna().sum().sum()==0
assert (df["Demand Units"]>=0).all()
assert (df["On Hand Units"]>=0).all()
assert df["Stockout"].isin([0,1]).all()
print("All inventory-demand quality tests passed.")
