import pandas as pd


df=pd.read_csv("corrected_data.csv")


#to find the missing values and drop them from data frame
df.dropna(subset=["price"],axis=0)
#if you put axis=0 it will delete the row and if you put axis=1 it will delete the column

#if you want to rewrite the table by removing dropped values
df.dropna(subset=["price"],axis=0,inplace=True)

#to convert the values of the column to numeric values
df['normalized-losses'] = pd.to_numeric(df['normalized-losses'], errors='coerce')#errors='coerce' is used to put NaN in case the value is not to_numeric

#to calculate mean of the column
mean = df['normalized-losses'].mean()

#replacing the NaN values of column with mean of the column
df['normalized-losses'] =df['normalized-losses'].fillna(mean)

#to save the new data to a new file
df.to_csv("corrected_data2.csv")
print(df)