## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
print(avengers.columns)
print(avengers.head(5))

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()

true_avengers = avengers[avengers["Year"]>1959]

## 5. Consolidating Deaths ##

def clean_deaths(row):
    cols = ["Death1","Death2","Death3","Death4","Death5"]
    deaths = 0
    for col in cols:
        if row[col] == "YES":
            deaths += 1
    return deaths

true_avengers["Deaths"] = true_avengers.apply(clean_deaths, axis=1)

## 6. Verifying Years Since Joining ##

joined_accuracy_count  = 0

joined_accuracy_count = sum(true_avengers["Years since joining"]==(2015-true_avengers["Year"]))
