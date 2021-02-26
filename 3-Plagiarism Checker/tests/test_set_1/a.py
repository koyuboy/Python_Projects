import matplotlib.pyplot as mtp
import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


if __name__ == "__main__":
    cwd = os.getcwd()
    data = pd.read_csv(cwd + '/Companies.csv')
    state = data.iloc[:,3].values
    stateInt = []
    for row in state:
        stateInt.append(sum(bytearray(row, encoding = 'utf8')))


    x = data.iloc[:,:-2].values # independent variables except state
    # add state to data columns
    x_new = []
    for t in range(len(x)):
        x_new.append(np.append(x[t], stateInt[t]))

    x = np.array(x_new) # independent variables
    y = data.iloc[:,-1].values # dependent variable(profit)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 0)

    regressor = LinearRegression()
    regressor.fit(x_train, y_train)
    
    y_pred = regressor.predict(x_test)
    x_pred = regressor.predict(x_train)
   
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