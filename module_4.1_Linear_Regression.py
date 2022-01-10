from sklearn.linear_model import LinearRegression
import pandas as pd

df=pd.read_csv("corrected_data4.csv")

df["price"]=pd.to_numeric(df["price"],errors='coerce')
df["highway-mpg"]=pd.to_numeric(df["price"],errors='coerce')
lm=LinearRegression()

x=df[['highway-mpg']]
y=df[['price']]

lm.fit(x, y)