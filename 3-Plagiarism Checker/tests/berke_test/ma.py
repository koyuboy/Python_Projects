import matplotlib.pyplot as mtp
import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


if __name__ == "__main__":
    data_set = pd.read_csv('Companies.csv')

    rdspend = data_set.iloc[:,0].values
    administration = data_set.iloc[:,1].values
    marketing_spend = data_set.iloc[:,2].values
    stateString = data_set.iloc[:,3].values
    print(stateString)
    x = np.empty([len(rdspend), 4], dtype=int)
    # california 1, new york 2, florida 3,
    for t in range(len(stateString)):
        tt = 0
        if stateString[t] == "California":
            tt = 1
        elif stateString[t] == "New York":
            tt = 2
        else:
            tt = 3
        x[t][0] = rdspend[t]
        x[t][1] = administration[t]
        x[t][2] = marketing_spend[t]
        x[t][3] = tt

    # ind. var = x 
    # dep. var = y
    y = data_set.iloc[:,4].values
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 0)

    regressor = LinearRegression()
    regressor.fit(x_train, y_train)

    y_pred = regressor.predict(x_test)
    x_pred = regressor.predict(x_train)

    print(regressor.coef_)

    dmp = np.arange(len(x_pred))
    mtp.scatter(dmp, y_train, color = "green") # real values 
    mtp.scatter(dmp, x_pred, color = "red" ) # after trained values
    mtp.title("Prediction")
    mtp.xlabel("Company Index")
    mtp.ylabel("Profit")
    mtp.show()

    dmp = np.arange(len(y_test))
    mtp.scatter(dmp, y_test, color = "green") # real values 
    mtp.scatter(dmp, y_pred, color = "blue") # after trained values
    mtp.title("Prediction")
    mtp.xlabel("Company Index")
    mtp.ylabel("Profit")
    mtp.show()

    mtp.scatter(x_test[:,0], y_test, color = "blue")
    mtp.title("Companies Profit Prediction")
    mtp.xlabel("RD")
    mtp.ylabel("Profit")
    mtp.show()

    mtp.scatter(x_test[:,1], y_test, color = "blue")
    mtp.title("Companies Profit Prediction")
    mtp.xlabel("Administration")
    mtp.ylabel("Profit")
    mtp.show()

    mtp.scatter(x_test[:,2], y_test, color = "blue")
    mtp.title("Companies Profit Prediction")
    mtp.xlabel("Marketing")
    mtp.ylabel("Profit")
    mtp.show()

    mtp.scatter(x_test[:,3], y_test, color = "blue")
    mtp.title("Companies Profit Prediction")
    mtp.xlabel("State")
    mtp.ylabel("Profit")
    mtp.show()

    