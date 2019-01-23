## 2. Introduction To The Data ##

import pandas as pd
data = pd.read_csv("AmesHousing.txt", delimiter="\t")
train = data.iloc[:1460]
test = data.iloc[1460:]
data.info()
target="SalePrice"

data.isnull().sum()

## 3. Simple Linear Regression ##

import matplotlib.pyplot as plt
# For prettier plots.
import seaborn as sns

fig = plt.figure(figsize=(16,30))

ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

data.plot(x="Garage Area", y="SalePrice", ax=ax1, kind="scatter")
data.plot(x="Gr Liv Area", y="SalePrice", ax=ax2, kind="scatter")
data.plot(x="Overall Cond", y="SalePrice", ax=ax3, kind="scatter")

plt.show()

## 5. Using Scikit-Learn To Train And Predict ##

from sklearn.linear_model import LinearRegression

model1 = LinearRegression()

model1.fit(train[["Gr Liv Area"]],train["SalePrice"])

a1 = model1.coef_
a0 = model1.intercept_

## 6. Making Predictions ##

import numpy as np
from sklearn.metrics import mean_squared_error

lr = LinearRegression()
lr.fit(train[['Gr Liv Area']], train['SalePrice'])

train_prediction = lr.predict(train[["Gr Liv Area"]])
train_rmse = np.sqrt(mean_squared_error(train_prediction,train["SalePrice"]))


test_prediction = lr.predict(test[["Gr Liv Area"]])
test_rmse = np.sqrt(mean_squared_error(test_prediction,test["SalePrice"]))

## 7. Multiple Linear Regression ##

cols = ['Overall Cond', 'Gr Liv Area']

lm = LinearRegression()

lm.fit(train[cols],train["SalePrice"])

train_predictions = lm.predict(train[cols])
test_predictions = lm.predict(test[cols])

train_rmse_2 = np.sqrt(mean_squared_error(train_predictions,train["SalePrice"]))

test_rmse_2 = np.sqrt(mean_squared_error(test_predictions,test["SalePrice"]))