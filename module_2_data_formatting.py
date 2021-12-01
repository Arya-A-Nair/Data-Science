import pandas as pd

df=pd.read_csv("corrected_data2.csv")
df=df.drop('Unnamed: 0.1',axis=1)
df=df.drop('Unnamed: 0',axis=1)

df["city-mpg"]=235/df["city-mpg"]
df.rename(columns={"city-mpg":"city-L/100Km"},inplace=True)

df.to_csv("corrected_data3.csv")
print (df)