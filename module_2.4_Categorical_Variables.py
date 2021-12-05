import pandas as pd
import numpy as np

df=pd.read_csv("corrected_data4.csv")

#to convert two categories into binary values
pd.get_dummies(df["fuel-type"])



