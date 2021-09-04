#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import metrics
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import cross_val_score


# In[2]:


df = pd.read_csv(r'bike_sharing_hours.csv')


# In[3]:


df.head()


# In[4]:


df.dtypes


# ### Pre-processing of data

# In[6]:


# date time conversion
df['dteday'] = pd.to_datetime(df.dteday)

# categorical variables
df['season'] = df.season.astype('category')
df['holiday'] = df.holiday.astype('category')
df['weekday'] = df.weekday.astype('category')
df['weathersit'] = df.weathersit.astype('category')
df['workingday'] = df.workingday.astype('category')
df['mnth'] = df.mnth.astype('category')
df['yr'] = df.yr.astype('category')
df['hr'] = df.hr.astype('category')


# ## Question-1

# 1. Are the average number of rented bikes in first 7 days of months different significantly between first 6 months Vs last 6 months of the year ? [consider column cnt]

# In[11]:


fig,ax = plt.subplots()
sns.pointplot(data=df[['mnth',
                           'cnt',
                           'weekday']],
              x='mnth',
              y='cnt',
              hue='weekday',
              ax=ax)
ax.set(title="Weekday wise  distribution of counts")


# ## Yes, it is different. In first six months it is increasing while in last six months it is decreasing.

# Q2-Find the average temperature [consider column temp] in the first quarter of the year . Has this changed significantly in the third quarter of the year ?

# In[14]:


df['mnth'].unique()


# In[15]:


# first quarter= 1,2,3 months and third quarter is 7,8,9 months
df['quarter'] = df['mnth'].apply(lambda x:'Q1' if x==1 else('Q1' if x==2 else('Q1' if x==3 else('Q3' if x==7 else('Q3' if x==8 else('Q3' if x==9 else None))))) )


# In[16]:


df['quarter'].unique()


# In[18]:


df.groupby('quarter').temp.mean()


# Yes average temperature average temperature in the first quarter has changed significantly from the third quarter Q1=.31 and Q3=.69

# ## 3. Does it matter which weekday it is , when it comes to causally rented bikes ? [consider column casual]

# In[22]:


fig,ax = plt.subplots()
sns.pointplot(data=df[['weekday',
                           'casual'
                           ]],
              x='weekday',
              y='casual',
              
              ax=ax)
ax.set(title="Weekday wise monthly distribution of counts")


# In[23]:


## Yes, in the 3rd weekday casual takes the least value while it takes the highest value in the 1st and the 7th week


# # Q2- find all possible solutions of system of these linear equations :

# $$ 2x + 3y + 4z^2 = 23 <br>
# 
#  y^2 - x^2 = 3 $$

# In[31]:


import numpy as np

m_list = [[2,3,4], [2,-2]]
A = np.array(m_list)


# In[ ]:





# In[ ]:





# # Q3 - Do weather situations affect bike renting behaviours . Show me visually . Consider columns [ temp , hum , windspeed and cnt]

# In[25]:


corrMatt = df[['temp',
                    'hum', 
                    'windspeed', 
                    'cnt', 'weathersit' 
                    ]].corr()

mask = np.array(corrMatt)
# Turning the lower-triangle of the array to false
mask[np.tril_indices_from(mask)] = False
fig,ax = plt.subplots()
sns.heatmap(corrMatt, 
            mask=mask,
            vmax=.8, 
            square=True,
            annot=True,
            ax=ax)


# In[26]:


fig,ax = plt.subplots()
sns.pointplot(data=df[['weathersit',
                           'temp'
                           ]],
              x='weathersit',
              y='temp',
              
              ax=ax)
ax.set(title="Weather vs temp")


# In[27]:


fig,ax = plt.subplots()
sns.pointplot(data=df[['weathersit',
                           'hum'
                           ]],
              x='weathersit',
              y='hum',
              
              ax=ax)
ax.set(title="Weather vs hum")


# In[28]:


fig,ax = plt.subplots()
sns.pointplot(data=df[['weathersit',
                           'cnt'
                           ]],
              x='weathersit',
              y='cnt',
              
              ax=ax)
ax.set(title="Weather vs count")


# In[29]:


fig,ax = plt.subplots()
sns.pointplot(data=df[['weathersit',
                           'windspeed'
                           ]],
              x='weathersit',
              y='windspeed',
              
              ax=ax)
ax.set(title="Weather vs windspeed")


# In[30]:


## weather has most significant on temp, humidity and count while it does not have a significant affect on windspeed. Inverse relation holds between tem and weather and positive relation between humidity and weahersit 


# In[ ]:




