import pandas as pd
import numpy as np

df=pd.read_csv("corrected_data4.csv")

pd.get_dummies(df["fuel-type"])
print(df)


