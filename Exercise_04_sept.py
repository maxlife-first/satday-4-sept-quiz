#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import numpy as np
import pandas as pd


# In[2]:


file='bike_sharing_hours.csv'


# In[3]:


data=pd.read_csv(file)


# In[4]:


data.shape


# In[5]:


data.head()


# In[6]:


data.tail()


# In[8]:


data.info()


# In[18]:


data['mnth'].value_counts()


# # QUESTION 1 B PART

# In[61]:


df1=data[(data['mnth']==1)|(data['mnth']==2)|(data['mnth']==3)]


# In[62]:


df1.shape


# In[71]:


df1['temp'].mean()


# In[63]:


df2=data[(data['mnth']==7)|(data['mnth']==8)|(data['mnth']==9)]


# In[64]:


df2.shape


# In[65]:


from scipy.stats import levene


# In[66]:


levene(df1['temp'],df2['temp'])


# In[67]:


# Since p value is less than the significance level of 0.05, so we do not accept the null hypothesis and conclude that 
# variance of the two samples are not equal.


# In[68]:


from scipy.stats import ttest_ind


# In[69]:


ttest_ind(df1['temp'],
          df2['temp'],
          equal_var=False)


# In[29]:


# Since the p value is less than the significance level of 0.05, so we do not accept the null hypothesis and conclude that 
# there is a significant difference in temperatures in first and third quarter


# # PART C

# In[32]:


weekday_grps=[data.loc[data['weekday']==w,'casual'].values 
              
              for w in data['weekday'].unique() ]


# In[33]:


from scipy.stats import f_oneway


# In[34]:


f_oneway(*weekday_grps)


# In[35]:


# Since the p value is less than the significance level of 0.05, so we do not accept the null hypothesis and conclude that 
# there is a significant difference between various weekdays for count of casual rented bikes


# # PART A

# In[37]:


df1=data[(data['mnth']==1)|(data['mnth']==2)|(data['mnth']==3)|(data['mnth']==4)|(data['mnth']==5)|(data['mnth']==6)]


# In[38]:


df2=data[(data['mnth']==7)|(data['mnth']==8)|(data['mnth']==9)|(data['mnth']==10)|(data['mnth']==11)|(data['mnth']==12)]


# In[72]:


df1['dteday']=pd.to_datetime(df1['dteday'], infer_datetime_format=True)


# In[73]:


df2['dteday']=pd.to_datetime(df2['dteday'], infer_datetime_format=True)


# In[39]:


from scipy.stats import ttest_rel


# In[57]:


levene(df1['cnt'],df2['cnt'])


# In[58]:


#Since p value is less than the significance level of 0.05, so we do not accept the null hypothesis and conclude that 
# variance of the two samples are not equal


# In[59]:


ttest_ind(df1['cnt'],
          df2['cnt'],
          equal_var=False)


# In[60]:


# Since the p value is less than the significance level of 0.05, so we do not accept the null hypothesis and conclude that 
# there is a significant difference between average numver of bikes rented in first 6 months and last 6 months


# # QUESTION 3

# In[40]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[44]:


sns.jointplot(x="hum", y="cnt", 
              data=data,
              kind="hex",size=10,color="g")


# In[41]:


sns.jointplot(x="temp", y="cnt", data=data)


# In[47]:


sns.jointplot(x="windspeed", y="cnt", 
              data=data,
              kind="hex",size=10,color="r")


# In[49]:


sns.lmplot('cnt', 'windspeed', 
           data=data,palette="Set1")


# In[50]:


sns.boxplot(y='cnt',data=data)


# In[51]:


sns.boxplot(y='hum',data=data)


# In[52]:


sns.boxplot(y='temp',data=data)


# In[53]:


sns.boxplot(y='windspeed',data=data)


# # QUESTION 2

# # Doubt - The equations are of non linear nature 

# In[ ]:




