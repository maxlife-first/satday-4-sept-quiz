#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import numpy as np
import pandas as pd
import datetime


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


file=r"D:\Sukreet\Training\Material\Sat exercise\bike_sharing_hours.csv"
data=pd.read_csv(file)


# In[4]:


data


# In[5]:


#1.1


# In[6]:


data.dteday = pd.to_datetime(data.dteday)


# In[8]:


from scipy.stats import levene


# In[9]:


levene(data.loc[(data['mnth']<7)&(data['dteday'].dt.day<=7),'cnt'],data.loc[(data['mnth']>=7)&(data['dteday'].dt.day<=7),'cnt'])


# In[ ]:


# this means variances are not equal


# In[10]:


from scipy.stats import ttest_ind


# In[13]:


ttest_ind(data.loc[(data['mnth']<7)&(data['dteday'].dt.day<=7),'cnt'],
          data.loc[(data['mnth']>=7)&(data['dteday'].dt.day<=7),'cnt'],
          equal_var=False)


# In[ ]:


#Since, pvalue<0.05, we reject H0 and thus there is a difference in average number of rented bikes in first 7 days of months for first 6 months Vs last 6 months of the year


# In[ ]:





# In[ ]:


#1.2


# In[23]:


levene(data.loc[(data['mnth']<4),'temp'],data.loc[(data['mnth'].isin(range(7,10))),'temp'])


# In[24]:


# this means variances are not equal, let's proceed.


# In[25]:


ttest_ind(data.loc[(data['mnth']<4),'temp'],
          data.loc[(data['mnth'].isin(range(7,10))),'temp'],
          equal_var=False)


# In[ ]:


#Since, pvalue<0,05, we reject H0 and thus the avg temp has changed significantly in 3rd qtr from 1st qtr.


# In[ ]:





# In[ ]:


#1.3


# In[26]:


data['weekday'].unique()


# In[27]:


weekday_grps=[data.loc[data['weekday']==q,'casual'].values 
              
              for q in data['weekday'].unique() ]


# In[28]:


data['weekday'].value_counts()


# In[29]:


from scipy.stats import f_oneway


# In[30]:


f_oneway(*weekday_grps)


# In[ ]:


# Since, p-value<0.05 we reject H0 and conclude that it matters what weekday it is for casually rented bikes.

