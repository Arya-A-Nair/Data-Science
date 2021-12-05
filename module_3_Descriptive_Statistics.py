import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("corrected_data.csv")
df.drop("Unnamed: 0",axis=1,inplace=True)

df.describe()

drive_wheel_counts=df["drive-wheels"].value_counts()



df.describe()