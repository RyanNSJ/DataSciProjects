## 1. Missing Values ##

import pandas as pd
data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

numerical_train = train.select_dtypes(include=["int", "float"])
numerical_train = numerical_train.drop(["PID","Year Built","Year Remod/Add","Garage Yr Blt","Mo Sold","Yr Sold"], axis=1)
null_series = numerical_train.isnull().sum()
full_cols_series = null_series[null_series==0]
print(full_cols_series)

## 2. Correlating Feature Columns With Target Column ##

train_subset = train[full_cols_series.index]

all_corrs = train_subset.corr()

sorted_corrs = abs(all_corrs["SalePrice"]).sort_values(ascending=True)

## 3. Correlation Matrix Heatmap ##

import seaborn as sns
import matplotlib.pyplot as plt

strong_corrs = sorted_corrs[sorted_corrs > 0.3]
corrmat = train_subset[strong_corrs.index].corr()
sns.heatmap(corrmat)

## 4. Train And Test Model ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

final_corr_cols = strong_corrs.drop(['Garage Cars', 'TotRms AbvGrd'])
features = final_corr_cols.drop(['SalePrice']).index
target = 'SalePrice'

test = test[final_corr_cols.index]
clean_test = test.dropna(axis=0)

lm = LinearRegression()
lm.fit(train[features],train[target])
train_predictions = lm.predict(train[features])
train_rmse = np.sqrt(mean_squared_error(train["SalePrice"],train_predictions))

test_predictions = lm.predict(clean_test[features])
test_rmse = np.sqrt(mean_squared_error(clean_test["SalePrice"],test_predictions))

## 5. Removing Low Variance Features ##

train[features] = (train[features]-train[features].min())/(train[features].max()-train[features].min())
print(train[features].min())
print(train[features].max())
sorted_vars = train[features].var().sort_values()
print(sorted_vars)

## 6. Final Model ##

features = features.drop(["Open Porch SF"])
lm = LinearRegression()
lm.fit(train[features],train[target])
train_predictions = lm.predict(train[features])
test_predictions = lm.predict(clean_test[features])
train_rmse_2 = np.sqrt(mean_squared_error(train_predictions,train[target]))
test_rmse_2 = np.sqrt(mean_squared_error(test_predictions,clean_test[target]))
print(train_rmse_2)
print(test_rmse_2)
print(features)