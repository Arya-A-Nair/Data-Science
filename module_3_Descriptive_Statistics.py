import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("corrected_data.csv")
df.drop("Unnamed: 0",axis=1,inplace=True)

df.describe()

#to get the number of FWD,RWD and 4WD cars
drive_wheel_counts=df["drive-wheels"].value_counts()


#boxplot method
df['price'] = pd.to_numeric(df['price'], errors='coerce')
sns.boxplot(x="drive-wheels",y="price",data=df)

#Scatter-Plot method
y=df["engine-size"]
x=df["price"]
plt.scatter(x,y)
plt.title("Engine Size vs Price")
plt.ylabel("Engine-Size")
plt.xlabel("Price")