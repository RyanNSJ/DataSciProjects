## 2. Calculating differences ##

female_diff = (10771-16280.5)/16280.5

male_diff = (21790-16280.5)/16280.5

## 3. Updating the formula ##

female_diff = (10771-16280.5)**2 / 16280.5
male_diff = (21790-16280.5)**2 / 16280.5
gender_chisq = female_diff+male_diff

## 4. Generating a distribution ##

chi_squared_values = []

for i in range(1000):
    Uvec = numpy.random.random((32561,))
    Uvec[Uvec < .5] = 0
    Uvec[Uvec >= .5] = 1
    male_count = len(Uvec[Uvec==0])
    female_count = len(Uvec[Uvec==1])
    male_diff = (male_count-16280.5)**2 / 16280.5
    female_diff = (female_count-16280.5)**2 / 16280.5
    chi_squared = male_diff+female_diff
    chi_squared_values.append(chi_squared)

plt.hist(chi_squared_values)
    

## 6. Smaller samples ##

female_diff = (107.71-162.805)**2 / 162.805
male_diff = (217.90-162.805)**2 / 162.805
gender_chisq = male_diff+female_diff

## 7. Sampling distribution equality ##

chi_squared_values = []

for i in range(1000):
    Uvec = numpy.random.random((300,))
    Uvec[Uvec<.5] = 0
    Uvec[Uvec>=.5] = 1
    male_count = len(Uvec[Uvec==0])
    female_count = len(Uvec[Uvec==1])
    male_diff = (male_count-150)**2 / 150
    female_diff = (female_count-150)**2 / 150
    chi_squared = male_diff+female_diff
    chi_squared_values.append(chi_squared)
    
plt.hist(chi_squared_values)

## 9. Increasing degrees of freedom ##

diffs = []
observed = [27816, 3124, 1039, 311, 271]
expected = [26146.5, 3939.9, 944.3, 260.5, 1269.8]

for i, obs in enumerate(observed):
    exp = expected[i]
    diff = (obs - exp) ** 2 / exp
    diffs.append(diff)
    
race_chisq = sum(diffs)

## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np

race_obs = np.array([27816, 3124, 1039, 311, 271])
race_exp = np.array([26146.5, 3939.9, 944.3, 260.5, 1269.8])

chisquare_value, race_pvalue = chisquare(race_obs,race_exp)