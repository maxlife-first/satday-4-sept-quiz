#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd
import numpy as np
from scipy.stats import ttest_rel
from scipy.stats import ttest_ind


# In[5]:


df=pd.read_csv('C:/Users/skhom4875/Desktop/Training/satday-4-sept-quiz/bike_sharing_hours.csv')


# In[6]:


df.head()


# In[8]:


df.shape


# In[54]:


df.mnth.value_counts()


# In[10]:


df.info()


# In[12]:


df['dteday']=pd.to_datetime(df['dteday'])


# In[13]:


df['dteday'].describe()


# In[29]:


import datetime as dt


# In[55]:


#extracting cnt for first 6 months
ls=[]
for i in range(len(df)):
    
    if df.dteday[i].month in [1,2,3,4,5,6] and  (df.dteday[i].day < 8):  
        ls.append(df['cnt'][i])


# In[59]:


#extracting cnt for last 6 months
ls2=[]
for i in range(len(df)):
    
    if df.dteday[i].month in [7,8,9,10,11,12] and  (df.dteday[i].day < 8):  
        ls2.append(df['cnt'][i])


# In[61]:


len(ls)


# In[62]:


len(ls2)


# In[67]:


from scipy.stats import levene
levene(ls,ls2)


# We  reject the null hypothesis. Variance is not equal

# In[83]:


#We will perform unpaired t test
ttest_ind(ls,ls2,equal_var=False)


# There is significant difference between average number of rented bikes in first 7 days of months for first 6 months Vs last 6 months of the year 

# In[72]:


#q1.2 unpaired t test
ls=[]
for i in range(len(df)):
    
    if df.dteday[i].month <=3: 
        ls.append(df['temp'][i])

ls2=[]
for i in range(len(df)):
    
    if df.dteday[i].month in [7,8,9]:  
        ls2.append(df['temp'][i])


# In[73]:


levene(ls,ls2)


# In[74]:


# Variance is not equal
ttest_ind(ls,ls2,equal_var=False)


# We reject the null hypothesis and conclude that average temp has changed significantly in the third quarter as compared to the first quarter
# 

# In[75]:


#q.1.3
#ANOVA
df.weekday.unique()


# In[76]:


weekday_grp=[df.loc[df['weekday']==q,'casual'].values
    for q in df['weekday'].unique()
]


# In[78]:


from scipy.stats import f_oneway


# In[79]:


f_oneway(*weekday_grp)


# We reject the null hypothesis and conclude atleast one weekday differs significantly 

# In[80]:


from statsmodels.stats.multicomp import pairwise_tukeyhsd


# In[81]:


tukey = pairwise_tukeyhsd(endog=df['casual'],    
                          groups=df['weekday'],   
                          alpha=0.05)


# In[82]:


tukey.summary()


# In[41]:


#temp , hum , windspeed
import seaborn as sns
subset=df[['temp','hum','windspeed','cnt']]

sns.heatmap(subset.corr(),annot=True)


# ### Weather situation does affect bike renting behaviour. Temperature has the most effect while humidity doesn't affect it at all.

# In[ ]:




