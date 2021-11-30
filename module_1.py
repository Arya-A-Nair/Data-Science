import pandas as pd      


#to read file in csv format
df=pd.read_csv("imports-85.data", header=None)


headers=['symboling','normalized-losses','make','fuel-type','aspiration','num-of-doors','body-style','drive-wheels','engine-location','wheel-base','length',' width','height','curb-weight','engine-type','num-of-cylinders','engine-size','fuel-system','bore','stroke','compression-ratio','horsepower','peak-rpm','city-mpg','highway-mpg','price']

#to assign the header list to columns of the data frame
df.columns = headers

#to display the data type of each and every columns
df.dtypes

#to get conscise summary of a data frame
df.info 

#to get statistics of a data frame
df.describe

#to store the modified csv file
df.to_csv("corrected_data.csv")