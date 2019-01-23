## 2. Grouped Bar Plots ##

import seaborn as sns
sns.countplot(x = 'Exp_ordinal', hue = 'Pos', data = wnba,
              order = ['Rookie', 'Little experience', 'Experienced', 'Very experienced', 'Veteran'],
              hue_order = ['C', 'F', 'F/C', 'G', 'G/F']
             )

## 3. Challenge: Do Older Players Play Less? ##

sns.countplot(x = 'age_mean_relative', hue = 'min_mean_relative', data = wnba)
result = 'rejection'

## 4. Comparing Histograms ##

import matplotlib.pyplot as plt
wnba[wnba.Age >= 27]['MIN'].plot.hist(histtype = 'step', label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.hist(histtype = 'step', label = 'Young', legend = True)
plt.axvline(497, label = 'Average')
plt.legend()

## 5. Kernel Density Estimate Plots ##

import matplotlib.pyplot as plt

wnba[wnba.Age >= 27]['MIN'].plot.kde(label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.kde(label = 'Young', legend = True)
plt.axvline(497, label = 'Average')
plt.legend()
plt.show()

## 7. Strip Plots ##

sns.stripplot(x = 'Pos', y = 'Weight', data = wnba, jitter = True)
plt.show()

## 8. Box plots ##

sns.boxplot(x = 'Pos', y = 'Weight', data = wnba)

## 9. Outliers ##

iqr = wnba["Games Played"].describe()["75%"] - wnba["Games Played"].describe()["25%"]
lower_bound = 22 - (1.5 * iqr)
upper_bound = 29 + (1.5 * iqr)
outliers_low = sum(wnba['Games Played'] < lower_bound) # True values will count as 1 in the summation
outliers_high = sum(wnba['Games Played'] > upper_bound)

sns.boxplot(wnba['Games Played'])