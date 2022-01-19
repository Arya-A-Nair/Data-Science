from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression as lr

Rsqu_test=[]

order=[1,2,3,4]

for n in order:
    pr=PolynomialFeatures(degree=n)#degree=n means that we will use the polynomial features of degree n
    
    x_train_pr=pr.fit_transform(x_train[["horsepower"]])
    x_test_pr=pr.fit_transform(x_test[["horsepower"]])

    lr.fit(x_train_pr,y_train)
    Rsqu_test.append(lr.score(x_test_pr,y_test))