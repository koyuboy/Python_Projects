import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


if __name__ == "__main__":
    cwd = os.getcwd()
    data = pd.read_csv(cwd + '/Companies.csv')

    x = data.iloc[:,:-1].values
    ct = ColumnTransformer([("State", OneHotEncoder(), [3])], remainder = 'passthrough')
    x = ct.fit_transform(x)
    y = data.iloc[:,-1].values # dependent variable(profit)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 0)

    regressor = LinearRegression()
    regressor.fit(x_train, y_train)
    
    y_pred = regressor.predict(x_test)
    x_pred = regressor.predict(x_train)


    plt.scatter(x_train[:,3], y_train, color = "green") #rd
    plt.scatter(x_train[:,4], y_train, color = "cyan") #administration
    plt.scatter(x_train[:,5], y_train, color = "yellow") # marketing
    plt.xlabel("Independent Variables Values")
    plt.ylabel("Profit")
    plt.show()


    plt.scatter(x_test[:,3], y_test, color = "green") #rd
    plt.scatter(x_test[:,4], y_test, color = "cyan") #administration
    plt.scatter(x_test[:,5], y_test, color = "yellow") # marketing
    plt.xlabel("Independent Variables Values")
    plt.ylabel("Profit")
    plt.show()


    index = np.arange(17)
    plt.scatter(index, y_test, color = "red") # real values 
    plt.scatter(index, y_pred, color = "cyan") # after trained values
    plt.xlabel("Index")
    plt.ylabel("Company Profit")
    plt.show()

    print(regressor.coef_)