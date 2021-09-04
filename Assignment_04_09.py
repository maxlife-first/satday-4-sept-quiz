# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 09:40:58 2021

@author: akhom4549
"""


import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import levene


df1 = pd.read_csv(r"C:\Users\akhom4549\Desktop\Training\bike_sharing_hours.csv")


# Ques1 solution

df1['dteday'] = pd.to_datetime(df1['dteday'])
df1['day'] = df1['dteday'].dt.day
levene(df1.loc[(df1['mnth']<=6)&(df1['day']<=7),'cnt'],df1.loc[(df1['mnth']>=7)&(df1['day']<=7),'cnt'])

# statistically significant since pvalue is 2.30E-08 hence we say the variances are not equal

from scipy.stats import ttest_ind
x = ttest_ind(df1.loc[(df1['mnth']<=6)&(df1['day']<=7),'cnt'],
          df1.loc[(df1['mnth']>=7)&(df1['day']<=7),'cnt'],
          equal_var=False)

# p value is 9.4E-20 hence we say the average number of rented bikes in first 7 days differ significantly

# average temperature in first quarter of the year taking first quarter as calendar quarter (Jan'-Mar)
df1[df1['mnth']<=3]['temp'].mean()
# this returns mean as 0.3106245

from scipy.stats import ttest_1samp
ttest_1samp(df1[(df1['mnth']>=7)&(df1['mnth']<=9)]['temp'],popmean=0.3106245)

# 0 p value is less than 0.05 hence we reject the null hypothesis, 
# hence we say that temperature has changed significantly

# checking for validation
df1[(df1['mnth']>=7)&(df1['mnth']<=9)]['temp'].mean()

from scipy.stats import chi2_contingency
k=pd.crosstab(df1['casual'],df1['weekday']).values
res=chi2_contingency(k)
res[1]

# p value os less than 0.05 hence we reject the null hypothesis
# i.e day of the week has relationship between casually rented bikes

# QUES 2 the equations shared in ques2 are non linear

# QUES 3 
# observations
# slight relation was observed with temperature, higher the temperature higher the sales

sns.heatmap(df1[['temp','hum','windspeed','cnt']].corr())
sns.jointplot(x="temp", y="cnt", data=df1.sample(1000),
              kind="hex",size=5,color="r")
df1.plot.scatter(x='temp',y='cnt')
sns.jointplot(x="hum", y="cnt", data=df1.sample(1000),
              kind="hex",size=5,color="r")
df1.plot.scatter(x='hum',y='cnt')
sns.jointplot(x="windspeed", y="cnt", data=df1.sample(1000),
              kind="hex",size=5,color="r")
df1.plot.scatter(x='windspeed',y='cnt')
