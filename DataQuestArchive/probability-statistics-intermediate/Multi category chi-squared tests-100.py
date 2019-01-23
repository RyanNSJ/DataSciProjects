## 2. Calculating expected values ##

males_over50k = .67 * .241 * 32561
males_under50k = .67 * .759 * 32561
females_over50k = .33 * .241 * 32561
females_under50k = .33 * .759 * 32561 


## 3. Calculating chi-squared ##

import numpy as np
import scipy.stats
obs = np.array([5249.8,2597.4,16533.5,8180.3])
exp  = np.array([6662,1179,15128,9592])
chisq_gender_income, chi_pval = scipy.stats.chisquare(exp,obs)


## 4. Finding statistical significance ##

import numpy as np
from scipy.stats import chisquare

observed = np.array([6662, 1179, 15128, 9592])
expected = np.array([5249.8, 2597.4, 16533.5, 8180.3])

chisq_value, pvalue_gender_income = chisquare(observed, expected)

## 5. Cross tables ##

import pandas as pd
table = pd.crosstab(income["sex"], [income["race"]])
print(table)

table = pd.crosstab(income["sex"], [income["high_income"]])
print(table)

## 6. Finding expected values ##

from scipy.stats import chi2_contingency

observed = np.array(pandas.crosstab(income["sex"],[income["race"]]))
chisq_value, pvalue_gender_race, df, expected = chi2_contingency(observed)