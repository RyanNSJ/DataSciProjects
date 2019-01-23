## 1. Recap ##

import pandas as pd

train_df = pd.read_csv("dc_airbnb_train.csv")
test_df = pd.read_csv("dc_airbnb_test.csv")

## 2. Hyperparameter optimization ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

hyper_params = list(range(1,6))
mse_values = []
features = ["accommodates","bedrooms","bathrooms","number_of_reviews"]

for k in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=k, algorithm="brute")
    knn.fit(train_df[features],train_df["price"])
    predictions = knn.predict(test_df[features])
    mse = mean_squared_error(test_df["price"],predictions)
    mse_values.append(mse)

print(mse_values)

## 3. Expanding grid search ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

hyper_params = list(range(1,21))
mse_values = []
features = ["accommodates","bedrooms","bathrooms","number_of_reviews"]

for k in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=k, algorithm="brute")
    knn.fit(train_df[features],train_df["price"])
    predictions = knn.predict(test_df[features])
    mse = mean_squared_error(test_df["price"],predictions)
    mse_values.append(mse)

print(mse_values)

## 4. Visualizing hyperparameter values ##

import matplotlib.pyplot as plt
%matplotlib inline

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
hyper_params = [x for x in range(1, 21)]
mse_values = list()

for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse = mean_squared_error(test_df['price'], predictions)
    mse_values.append(mse)
    
plt.scatter(x=hyper_params,y=mse_values)
plt.show()

## 5. Varying features and hyperparameters ##

hyper_params = [x for x in range(1,21)]
mse_values = list()

features = list(train_df.columns)
features.remove("price")

for k in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=k, algorithm="brute")
    knn.fit(train_df[features],train_df["price"])
    predictions = knn.predict(test_df[features])
    mse = mean_squared_error(test_df["price"],predictions)
    mse_values.append(mse)
    
plt.scatter(x=hyper_params,y=mse_values)
plt.show()

## 6. Practice the workflow ##

two_features = ['accommodates', 'bathrooms']
three_features = ['accommodates', 'bathrooms', 'bedrooms']
hyper_params = [x for x in range(1,21)]

# Append the first model's MSE values to this list.
two_mse_values = list()

# Append the second model's MSE values to this list.
three_mse_values = list()

two_hyp_mse = dict()
three_hyp_mse = dict()

for k in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=k, algorithm="brute")
    knn.fit(train_df[two_features],train_df["price"])
    predictions = knn.predict(test_df[two_features])
    mse = mean_squared_error(predictions,test_df["price"])
    two_mse_values.append(mse)

print(two_mse_values)
two_lowest_mse = min(two_mse_values)
two_lowest_k = 1
for i,mse in enumerate(two_mse_values):
    print(mse)
    print(two_lowest_mse)
    if mse!=two_lowest_mse:
        two_lowest_k += 1
        print(two_lowest_k)
    else:
        print(two_lowest_k)
        break

for k in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=k, algorithm="brute")
    knn.fit(train_df[three_features],train_df["price"])
    predictions = knn.predict(test_df[three_features])
    mse = mean_squared_error(predictions,test_df["price"])
    three_mse_values.append(mse)
    
three_lowest_mse = min(three_mse_values)
three_lowest_k = 1
for i,mse in enumerate(three_mse_values):
    if mse!=three_lowest_mse:
        three_lowest_k += 1
    else:
        break

two_hyp_mse[two_lowest_k] = two_lowest_mse
three_hyp_mse[three_lowest_k] = three_lowest_mse