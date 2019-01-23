## 3. Populations and Samples ##

question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')
parameter = wnba['Games Played'].max()
sample = wnba['Games Played'].sample(30, random_state = 1)
statistic = sample.max()
sampling_error = parameter - statistic

## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt

wnba = pd.read_csv('wnba.csv')

sample = wnba.sample(100, random_state=1)

outpls = []

for i in range(0,100):
    outpls.append(sample["PTS"].sample(10, random_state=i).mean())

plt.scatter(x=range(0,100),y=outpls)
plt.axhline(wnba["PTS"].mean())

## 7. Stratified Sampling ##

wnba["POINTS_PER_GAME"] = wnba["PTS"]/wnba["Games Played"]

# 5 Stratum
wnba_F = wnba.loc[wnba["Pos"]=="F"]
wnba_GF = wnba.loc[wnba["Pos"]=="G/F"]
wnba_G = wnba.loc[wnba["Pos"]=="G"]
wnba_C = wnba.loc[wnba["Pos"]=="C"]
wnba_FC = wnba.loc[wnba["Pos"]=="F/C"]

strata = [wnba_C,wnba_F,wnba_FC,wnba_GF,wnba_G]

strata_dict = {}

for stratum in strata:
    stratum_sample = stratum.sample(10, random_state=0)
    sample_mean = stratum_sample["POINTS_PER_GAME"].mean()
    strata_dict[stratum["Pos"].iloc[0]] = sample_mean

position_most_points = max(strata_dict, key=strata_dict.get)

## 8. Proportional Stratified Sampling ##

wnba_A = wnba.loc[wnba["Games Played"]<=12]
wnba_B = wnba.loc[(wnba["Games Played"]>12) & (wnba["Games Played"]<=22)]
wnba_C = wnba.loc[wnba["Games Played"]>22]

outpls = []

for i in range(0,100):
    sample_a = wnba_A.sample(1,random_state=i)
    sample_b = wnba_B.sample(2,random_state=i)
    sample_c = wnba_C.sample(7,random_state=i)
    sample = pd.concat([sample_a,sample_b,sample_c])
    mean = sample["PTS"].mean()
    outpls.append(mean)

plt.scatter(x=range(0,100), y=outpls)
plt.axhline(wnba["PTS"].mean())
    

## 10. Cluster Sampling ##

team_clusters = pd.Series(wnba["Team"].unique()).sample(4, random_state=0)
sampled_clusters = pd.DataFrame()

for team in team_clusters:
    sampled_clusters = pd.concat([sampled_clusters,wnba.loc[wnba["Team"]==team]])

sample_height_mean = sampled_clusters["Height"].mean()
sample_age_mean = sampled_clusters["Age"].mean()
sample_bmi_mean = sampled_clusters["BMI"].mean()
sample_points_mean = sampled_clusters["PTS"].mean()

pop_height_mean = wnba["Height"].mean()
pop_age_mean = wnba["Age"].mean()
pop_bmi_mean = wnba["BMI"].mean()
pop_points_mean = wnba["PTS"].mean()

sampling_error_height = pop_height_mean-sample_height_mean
sampling_error_age = pop_age_mean-sample_age_mean
sampling_error_BMI = pop_bmi_mean-sample_bmi_mean
sampling_error_points = pop_points_mean-sample_points_mean
