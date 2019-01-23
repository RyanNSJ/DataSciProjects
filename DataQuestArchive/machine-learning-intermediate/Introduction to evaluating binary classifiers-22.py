## 1. Introduction to the Data ##

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

admissions = pd.read_csv("admissions.csv")
model = LogisticRegression()
model.fit(admissions[["gpa"]], admissions["admit"])
labels = model.predict(admissions[["gpa"]])
admissions["predicted_label"] = labels
print(admissions["predicted_label"].value_counts())
print(admissions.head())

## 2. Accuracy ##

admissions["actual_label"] = admissions["admit"]
matches = admissions["predicted_label"]==admissions["actual_label"]
correct_predictions = admissions[matches]
print(correct_predictions.head())
accuracy = matches.sum()/matches.count()

## 4. Binary classification outcomes ##

true_positives = ((admissions["predicted_label"]==1) & (admissions["actual_label"]==1)).sum()
true_negatives = ((admissions["predicted_label"]==0) & (admissions["actual_label"]==0)).sum()

## 5. Sensitivity ##

# From the previous screen
true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])

false_negatives = ((admissions["predicted_label"]==0) & (admissions["actual_label"]==1)).sum()
sensitivity = true_positives/(true_positives+false_negatives)

## 6. Specificity ##

# From previous screens
true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])
false_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 1)
false_negatives = len(admissions[false_negative_filter])
true_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 0)
true_negatives = len(admissions[true_negative_filter])
false_positives = ((admissions["predicted_label"]==1) & (admissions["actual_label"]==0)).sum()

sensitivity = true_positives/(false_negatives+true_positives)
specificity = true_negatives/(false_positives+true_negatives)