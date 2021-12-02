import pandas as pd

#To read the data from the csv file
df=pd.read_csv("corrected_data3.csv")

'''
    Normalisation is the process of transforming the data into a range of values between 0 and 1.
    This is done to make the data easier to process and easier to compare.  
    There are 3 main ways to normalise the data
    1) Min-Max normalisation
        x' = (x - min(x)) / (max(x) - min(x))
    2) Z-score normalisation
        x' = (x - mean(x)) / std(x)
    3) Simple feature scaling
        x' = x / max(x)
'''
#Simple feature scaling
df["length"]=df["length"]/df["length"].max()


#Min-Max normalisation
df["length"]=(df["length"]-df["length"].min())/(df["length"].max()-df["length"].min())

#Z-score normalisation
df["length"]=(df["length"]-df["length"].mean())/df["length"].std()

#To write the data to the csv file
df.to_csv("corrected_data4.csv")