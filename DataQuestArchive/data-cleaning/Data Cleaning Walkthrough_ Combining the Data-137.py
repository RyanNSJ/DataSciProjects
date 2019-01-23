## 3. Condensing the Class Size Data Set ##

class_size = data["class_size"]

class_size = class_size.loc[class_size["GRADE "]=="09-12",:]

class_size = class_size.loc[class_size["PROGRAM TYPE"]=="GEN ED",:]

class_size.head()

## 5. Computing Average Class Sizes ##

import numpy as np

class_size = class_size.groupby("DBN").agg(np.mean)
data["class_size"] = class_size

print (data["class_size"].head())


## 7. Condensing the Demographics Data Set ##

data["demographics"] = data["demographics"].loc[data["demographics"]["schoolyear"]==20112012,:]
print(data["demographics"].head())

## 9. Condensing the Graduation Data Set ##

data["graduation"] = data["graduation"].loc[data["graduation"]["Demographic"]=="Total Cohort",:]
data["graduation"] = data["graduation"].loc[data["graduation"]["Cohort"]=="2006",:]

## 10. Converting AP Test Scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']

print (data["ap_2010"].dtypes)
for col in cols:
    data["ap_2010"][col] = pd.to_numeric(data["ap_2010"][col],errors="coerce")

data["ap_2010"].dtypes


## 12. Performing the Left Joins ##

combined = data["sat_results"]
print(combined.shape)
combined = combined.merge(data["ap_2010"],how="left",on="DBN")
print(combined.shape)
combined = combined.merge(data["graduation"],how="left",on="DBN")
print(combined.shape)

combined.head(10)

## 13. Performing the Inner Joins ##

print(combined.shape)
combined  = combined.merge(data["class_size"],how="inner",on="DBN")
print(combined.shape)
combined  = combined.merge(data["demographics"],how="inner",on="DBN")
print(combined.shape)
combined  = combined.merge(data["survey"],how="inner",on="DBN")
print(combined.shape)
combined  = combined.merge(data["hs_directory"],how="inner",on="DBN")
print(combined.shape)
print(combined.head(10))

## 15. Filling in Missing Values ##

mean = combined.mean()
combined = combined.fillna(mean)
combined = combined.fillna(0)

print(combined.head(10))

## 16. Adding a School District Column for Mapping ##

def first_two(s):
    return s[:2]

combined["school_dist"] = combined["DBN"].apply(first_two)

print(combined["school_dist"].head())