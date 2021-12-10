import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("corrected_data.csv")
df["price"]=pd.to_numeric(df["price"],errors='coerce')
df["peak-rpm"]=pd.to_numeric(df["peak-rpm"],errors='coerce')

#Positive linear correlation
sns.regplot(x="engine-size",y="price",data=df)
plt.ylim(0,)
#as the engine size increases the price increases. hence it is a good predictor of price.

#Negative linear correlation
sns.regplot(x="highway-mpg",y="price",data=df)
plt.ylim(0,)
#as the highway mpg decreases the price increases. hence it is a good predictor of price.

#weak linear correlation
sns.regplot(x="peak-rpm",y="price",data=df)
plt.ylim(0,)
#the slope of line is very less hence it is not a useful predictor of price.