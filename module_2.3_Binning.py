import pandas as pd
import numpy as np

df=pd.read_csv("corrected_data.csv")
df.dropna(axis = 1,inplace=True)
df['price'] = pd.to_numeric(df['price'], errors='coerce')
#print(df["price"])

bins=np.linspace(min(df["price"]), max(df["price"]),4)

group_names=["Low","Medium","High"]

df["price-binned"]=pd.cut(df["price"],bins,labels=group_names, include_lowest=True)

print(df["price-binned"])

df["price-binned"].to_csv("price_binned.csv")
