from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn.model_selection import cross_val_predict

#We us this function to divide the dataset into two categories
x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,test_size=0.3,random_state=0)
'''
x_train and y_train would be used to train the model
x_test and y_test will be used to understand the  error of the model we have created.
'''



#We will use the cross_val_score function to evaluate the model
scores = cross_val_score(lr,X=x_train,y=y_train,cv=3)
'''
cv=3 means that we will use 3 folds to evaluate the model
'''

np.mean(scores)


#We will use the cross_val_predict function to predict the values
predictions = cross_val_predict(lr,X=x_train,y=y_train,cv=3)
'''
This function will help us to predict the values of the test data
cv=3 means that we will use 3 folds to evaluate the model
'''
