## 2. Introduction to the data ##

import pandas as pd
dc_listings = pd.read_csv("dc_airbnb.csv")
print(dc_listings.iloc[0])

## 4. Euclidean distance ##

import numpy as np

first_distance = np.sqrt((3-dc_listings["accommodates"][0])**2)
print(first_distance)

## 5. Calculate distance for all observations ##

import numpy as np

all_distance = np.sqrt((3-dc_listings["accommodates"])**2)
dc_listings["distance"] = all_distance
dc_listings["distance"] = dc_listings["distance"].astype(int)
print(dc_listings["distance"].value_counts())
print(dc_listings["distance"].value_counts().sort_index())

## 6. Randomizing, and sorting ##

import numpy as np
np.random.seed(1)

new_index = np.random.permutation(len(dc_listings))
dc_listings = dc_listings.iloc[new_index]
dc_listings = dc_listings.sort_values("distance")
print(dc_listings["distance"].head(10))

## 7. Average price ##

stripped_commas = dc_listings["price"].str.replace(",","")
dc_listings["price"] = stripped_commas

stripped_dollars = dc_listings["price"].str.replace("$","")
dc_listings["price"] = stripped_dollars

dc_listings["price"] = dc_listings["price"].astype(float)

mean_price = dc_listings["price"].iloc[0:5].mean()
print(mean_price)

## 8. Function to make predictions ##

# Brought along the changes we made to the `dc_listings` Dataframe.
dc_listings = pd.read_csv('dc_airbnb.csv')
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]

def predict_price(new_listing):
    temp_df = dc_listings.copy()
    ## Complete the function.
    temp_df["distance"] = np.sqrt((new_listing-temp_df["accommodates"])**2)
    temp_df = temp_df.sort_values("distance")
    new_listing = temp_df["price"].iloc[0:5].mean()
    return(new_listing)

acc_one = predict_price(1)
acc_two = predict_price(2)
acc_four = predict_price(4)