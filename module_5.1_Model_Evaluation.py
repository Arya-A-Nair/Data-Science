from sklearn.model_selection import train_test_split

#We us this function to divide the dataset into two categories
x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,test_size=0.3,random_state=0)

'''
x_train and y_train would be used to train the model
x_test and y_test will be used to understand the  error of the model we have created.
'''