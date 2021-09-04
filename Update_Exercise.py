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


# In[7]:


data.info()


# In[8]:


data['mnth'].value_counts()


# # QUESTION 1 B PART

# In[9]:


df1=data[(data['mnth']==1)|(data['mnth']==2)|(data['mnth']==3)]


# In[10]:


df1.shape


# In[11]:


df1['temp'].mean()


# In[12]:


df2=data[(data['mnth']==7)|(data['mnth']==8)|(data['mnth']==9)]


# In[13]:


df2.shape


# In[14]:


from scipy.stats import ttest_1samp


# In[15]:


ttest_1samp(df2['temp'],popmean=0.310)


# In[16]:


# Since p value is less than the significance level of 0.05, so we do not accept the null hypothesis and conclude that 
# mean temperature in quarter 3 is different from mean temperature in quarter 1


# # PART C

# In[17]:


weekday_grps=[data.loc[data['weekday']==w,'casual'].values 
              
              for w in data['weekday'].unique() ]


# In[18]:


from scipy.stats import f_oneway


# In[19]:


f_oneway(*weekday_grps)


# In[20]:


# Since the p value is less than the significance level of 0.05, so we do not accept the null hypothesis and conclude that 
# there is a significant difference between various weekdays for count of casual rented bikes


# # PART A

# In[21]:


df1=data[(data['mnth']==1)|(data['mnth']==2)|(data['mnth']==3)|(data['mnth']==4)|(data['mnth']==5)|(data['mnth']==6)]


# In[22]:


df2=data[(data['mnth']==7)|(data['mnth']==8)|(data['mnth']==9)|(data['mnth']==10)|(data['mnth']==11)|(data['mnth']==12)]


# In[23]:


df1['dteday']=pd.to_datetime(df1['dteday'])


# In[24]:


df2['dteday']=pd.to_datetime(df2['dteday'])


# In[25]:


df1=df1[df1['dteday'].dt.day<=7]


# In[26]:


df2=df2[df2['dteday'].dt.day<=7]


# In[27]:


from scipy.stats import ttest_rel


# In[28]:


from scipy.stats import levene


# In[29]:


levene(df1['cnt'],df2['cnt'])


# In[30]:


#Since p value is less than the significance level of 0.05, so we do not accept the null hypothesis and conclude that 
# variance of the two samples are not equal


# In[32]:


from scipy.stats import ttest_ind


# In[33]:


ttest_ind(df1['cnt'],
          df2['cnt'],
          equal_var=False)


# In[34]:


# Since the p value is less than the significance level of 0.05, so we do not accept the null hypothesis and conclude that 
# there is a significant difference between average number of bikes rented in first 6 months and last 6 months
#(for first 7 days of month)


# # QUESTION 3

# In[35]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[36]:


sns.jointplot(x="hum", y="cnt", 
              data=data,
              kind="hex",size=10,color="g")


# In[37]:


sns.jointplot(x="temp", y="cnt", data=data)


# In[38]:


sns.jointplot(x="windspeed", y="cnt", 
              data=data,
              kind="hex",size=10,color="r")


# In[39]:


sns.lmplot('cnt', 'windspeed', 
           data=data,palette="Set1")


# In[40]:


sns.boxplot(y='cnt',data=data)


# In[41]:


sns.boxplot(y='hum',data=data)


# In[42]:


sns.boxplot(y='temp',data=data)


# In[43]:


sns.boxplot(y='windspeed',data=data)


# In[44]:


data.corr()


# In[45]:


#Temp has a slight positive relation with cnt and humidity has a negative relation with cnt(bike rentals)


# # QUESTION 2

# # Doubt - The equations are of non linear nature 

# In[ ]:




