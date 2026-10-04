import pandas as pd
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/"data/credit_risk_1200.csv")
# Illustrative portfolio score for demonstration only.
df["PD_decimal"]=df["PD %"]/100
df["Expected Loss EUR"]=df["Exposure EUR"]*df["PD_decimal"]*(df["LGD %"]/100)
df["Decision"]=df["Risk Band"].map({"Low":"STANDARD","Medium":"ENHANCED REVIEW","High":"MANUAL UNDERWRITING / RESTRUCTURE"})
print(df.groupby("Decision")["Exposure EUR"].sum().sort_values(ascending=False))
