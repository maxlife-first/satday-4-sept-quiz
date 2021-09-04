#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import seaborn as sns
from datetime import datetime
get_ipython().run_line_magic('matplotlib', 'inline')
from scipy.optimize import fsolve

file=r"D:\2. Learning\1. Trainings\Edvancer\Assignment 2\bike_sharing_hours.csv"
bike_data=pd.read_csv(file)
bike_data['day']=bike_data['dteday'].dt.day
bike_data['cnt'].mean()
bike_one=bike_data.loc[(bike_data['day']<=7) & (bike_data['mnth']<=6)]
bike_data.loc[(bike_data['day']<=7) & (bike_data['mnth']<=6)]['cnt'].mean()
bike_data.loc[(bike_data['day']<=7) & (bike_data['mnth']>6)]['cnt'].mean()

#Q1.a Are the average number of rented bikes in first 7 days of months different significantly between first 6 months Vs last 6 months of the year ? [consider column cnt]
#Yes 162.7 vs 213.6 in first 6 vs rest 6 in first 7 days of month


#Q1bFind the average temperature [consider column temp] in the first quarter of the year . Has this changed significantly in the third quarter of the year ?
#yes (0.69 vs 0.31)

q1=[1,2,3]
q2=[4,5,6]
q3=[7,8,9]
q4=[10,11,12]

bike_data.loc[(bike_data['mnth']<=3)]['temp'].mean()

bike_data.loc[(bike_data['mnth'].isin(q3))]['temp'].mean()

bike_data['casual'].mean()

bike_data.groupby(['weekday'])['casual'].mean()


#Q1c. Does it matter which weekday it is , when it comes to causally rented bikes ? [consider column casual]
#yes; casual rental higher on weekday =0,6



#Q3 Do weather situations affect bike renting behaviours . Show me visually . Consider columns [ temp , hum , windspeed and cnt]

sns.lmplot('temp', 'cnt', 
           data=bike_data,palette="Set1",
           fit_reg=True,order=2)


sns.lmplot('hum', 'cnt', 
           data=bike_data,palette="Set1",
           fit_reg=True,order=2)


sns.lmplot('windspeed', 'cnt', 
           data=bike_data,palette="Set1",
           fit_reg=True,order=2)


# # Q2

#2x + 3y + 4z^2 = 23
#y^2 - x^2 = 3


def solver_dk(a):
   x = a[0]
   y = a[1]
   z = a[2]

   F = np.empty((3))
   F[0] = 2*x+3*y+4*z**2-23
   F[1] = y**2 - x**2-3
   return F

zGuess = np.array([1,1,1])
a = fsolve(solver_dk,zGuess)
print(a)
