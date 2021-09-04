#!/usr/bin/env python
# coding: utf-8

# consider data bike_sharing in the repo . Respond with your conclusions [and code if needed ] for the following
# 
# Are the average number of rented bikes in first 7 days of months different significantly between first 6 months Vs last 6 months of the year ? [consider column cnt]
# Find the average temperature [consider column temp] in the first quarter of the year . Has this changed significantly in the third quarter of the year ?
# Does it matter which weekday it is , when it comes to causally rented bikes ? [consider column casual]

# In[1]:


import seaborn as sns
import numpy as np
import pandas as pd


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


bike = pd.read_csv('bike_sharing_hours.csv')


# In[4]:


bike.sample(10)


# In[5]:


bike.info()


# ### Are the average number of rented bikes in first 7 days of months different significantly between first 6 months Vs last 6 months of the year ? [consider column cnt]

# In[6]:


bike['dteday'] = pd.to_datetime(bike['dteday'])


# In[7]:


bike[['cnt','dteday','mnth']]


# In[8]:


bike['days']=bike.dteday.dt.day


# In[9]:


from scipy.stats import levene


# In[10]:


levene(bike.loc[bike['days']<8,'cnt'],bike.loc[bike['mnth']<7,'cnt'])


# In[11]:


from scipy.stats import ttest_ind


# In[14]:


ttest_ind(bike.loc[bike['days']<8,'cnt'],
          bike.loc[bike['mnth']<7,'cnt'],
          equal_var=False)


# H0:Means are same
# H1:Means are significantly different

# ##### Since pvalue<0.05, we must reject the null hypothesis and conclude that average number of rented bikes in first 7 days of months different significantly between first 6 months 

# In[17]:


ttest_ind(bike.loc[bike['days']<8,'cnt'],
          bike.loc[bike['mnth']>=7,'cnt'],
          equal_var=False)


# ##### Since pvalue<0.05, we must reject the null hypothesis and conclude that average number of rented bikes in first 7 days of months different significantly between last 6 months 

# ## 2 Find the average temperature [consider column temp] in the first quarter of the year . Has this changed significantly in the third quarter of the year ?

# In[18]:


bike


# In[19]:


bike['year'] = bike['dteday'].dt.year


# In[20]:


bike_qtr = bike[bike.mnth.isin([1,2,3,4])]


# In[21]:


bike_qtr.info()


# In[22]:


bike_qtr1 = bike_qtr.groupby(['year','mnth']).temp.mean().reset_index()


# In[23]:


bike_qtr_mean = bike_qtr1.groupby('year').temp.mean().reset_index()
bike_qtr_mean


# In[24]:


bike_qtr3 = bike[bike.mnth.isin([9,10,11,12])]


# In[25]:


bike_qtr3 = bike_qtr3.groupby(['year','mnth']).temp.mean().reset_index()


# In[26]:


bike_qtr3_mean = bike_qtr3.groupby('year').temp.mean().reset_index()


# In[27]:


bike_qtr_mean,bike_qtr3_mean


# In[28]:


from scipy.stats import levene


# In[29]:


levene(bike.loc[bike.mnth.isin([1,2,3,4]),'temp'],bike.loc[bike.mnth.isin([9,10,11,12]),'temp'])


# #### variance is different

# In[30]:


ttest_ind(bike.loc[bike.mnth.isin([1,2,3,4]),'temp'],
          bike.loc[bike.mnth.isin([9,10,11,12]),'temp'],
          equal_var=False)


# #### Since p value is less than 5% we reject null and conclude that avg temperatue means are significantly different for 1st and last quarter

# ### Does it matter which weekday it is , when it comes to causally rented bikes ? [consider column casual]

# In[31]:


bike.weekday.value_counts(dropna=False)


# In[32]:


bike[['weekday','dteday']].sample(50)


# ## Q3

# In[33]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[34]:


sns.jointplot(x="hum", y="cnt", 
              data=bike,
              kind="hex",size=10,color="g")


# In[35]:


sns.jointplot(x="temp", y="cnt", data=bike)


# In[36]:


sns.jointplot(x="windspeed", y="cnt", 
              data=bike,
              kind="hex",size=10,color="r")


# In[37]:


sns.lmplot('cnt', 'windspeed', 
           data=bike,palette="Set1")


# In[38]:


sns.boxplot(y='cnt',data=bike)


# In[39]:


sns.boxplot(y='hum',data=bike)


# In[40]:


sns.boxplot(y='temp',data=bike)


# In[ ]:




