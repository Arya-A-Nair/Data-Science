from sklearn.linear_model import LinearRegression
import pandas as pd

df=pd.read_csv("corrected_data4.csv")
#Converting values to numeric
df["price"]=pd.to_numeric(df["price"],errors='coerce')
df["highway-mpg"]=pd.to_numeric(df["price"],errors='coerce')

#declaring class of LinearRegression
lm=LinearRegression()

#fitting the data
x=df[['highway-mpg']]
y=df[['price']]
lm.fit(x, y)

#Getting the coefficients of the linear regression
lm.coef_()

#getting the intercept of the linear regression
lm.intercept_()