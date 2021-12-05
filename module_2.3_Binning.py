import pandas as pd
import numpy as np

df=pd.read_csv("corrected_data.csv")

#converting dtype=object to dtype=float64
df['price'] = pd.to_numeric(df['price'], errors='coerce')

#to get evenly spaced integers over a range of numbers
bins=np.linspace(min(df["price"]), max(df["price"]),4)

group_names=["Low","Medium","High"]

#to bin the data into 4 segments
df["price-binned"]=pd.cut(df["price"],bins,labels=group_names, include_lowest=True)


#to save the binned data to csv format
df["price-binned"].to_csv("price_binned.csv")
