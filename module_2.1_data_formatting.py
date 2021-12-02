import pandas as pd

#To read the data from a file, we use the read_csv() function.
df=pd.read_csv("corrected_data2.csv")

#to drop some of the columns, we use the drop() function.
df=df.drop('Unnamed: 0.1',axis=1)
df=df.drop('Unnamed: 0',axis=1)

#to change the value of each element in a column
df["city-mpg"]=235/df["city-mpg"]

#to change the name of a column
df.rename(columns={"city-mpg":"city-L/100Km"},inplace=True)

#To save the data to a file, we use the to_csv() function.
df.to_csv("corrected_data3.csv")
print (df)