import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("corrected_data.csv")

# to get a new data frame with the desired columns
df_test=df[['drive-wheels','body-style','price']]

#to chane datatype of price column
df_test['price']=pd.to_numeric(df_test['price'],errors='coerce')

#to group the rows with drive-wheels and body-style and get the average price
df_grp = df_test.groupby(['drive-wheels','body-style'],as_index=False).mean()

#convert the data into a pivot table
df_pivot=df_grp.pivot(index='drive-wheels',columns='body-style')

#to make a heat map of the data
plt.pcolor(df_pivot,cmap='RdBu')
plt.colorbar()
plt.show()


