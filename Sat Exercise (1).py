#!/usr/bin/env python
# coding: utf-8

# In[17]:


import seaborn as sns
import numpy as np
import pandas as pd
import datetime


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


file=r"D:\Sukreet\Training\Material\Sat exercise\bike_sharing_hours.csv"
data=pd.read_csv(file)


# In[26]:


data


# In[ ]:


#1.1


# In[35]:


data.dteday = pd.to_datetime(data.dteday)


# In[47]:


data.iloc[data['dteday'].day<7]


# In[5]:


from scipy.stats import levene


# In[43]:


levene(data.loc[(data['mnth']<7)&(data['dteday'].day<=7),'cnt'],data.loc[(data['mnth']>=7)&(data['dteday'].day<=7),'cnt'])


# In[ ]:


# this means variances are equal


# In[10]:


from scipy.stats import ttest_ind


# In[12]:


ttest_ind(data.loc[(data['mnth']<7)&(data['workingday']<=7),'cnt'],
          data.loc[(data['mnth']>=7)&(data['workingday']<=7),'cnt'],
          equal_var=True)


# In[ ]:





# In[ ]:


#1.2


# In[48]:


levene(data.loc[(data['mnth']<4),'temp'],data.loc[(data['mnth']>9),'temp'])


# In[ ]:


# this means variances are equal, let's proceed.


# In[49]:


ttest_ind(data.loc[(data['mnth']<4),'temp'],
          data.loc[(data['mnth']>9),'temp'],
          equal_var=True)


# In[ ]:


#Since, pvalue>0,05, we fail to reject H0 and thus the avg temp has not changed significantly in 3rd qtr from 1st qtr.


# In[ ]:





# In[ ]:


#1.3


# In[57]:


data['weekday'].unique()


# In[58]:


weekday_grps=[data.loc[data['weekday']==q,'casual'].values 
              
              for q in data['weekday'].unique() ]


# In[59]:


data['weekday'].value_counts()


# In[60]:


from scipy.stats import f_oneway


# In[63]:


f_oneway(*weekday_grps)


# In[ ]:


# SInce, p-value<0.05 we reject H0 and conclude that it matters what weekday it is for casually rented bikes.

