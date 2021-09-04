#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


# Question 1


# In[3]:


data=pd.read_csv("C:/Users/sghom4876/Desktop/Training/satday-4-sept-quiz/bike_sharing_hours.csv")


# In[4]:


data.shape


# In[5]:


data.head(2)


# In[75]:


df1=data.loc[data["mnth"] <= 3]


# In[76]:


df1.head(2)


# In[77]:


df2=pd.DataFrame(data.groupby(['mnth'])["temp"].mean())


# In[78]:


df2


# In[79]:


quat_1=df2[0:3].mean()
quat_1


# In[80]:


quat_3=df2[6:9].mean()
quat_3


# In[69]:


from scipy.stats import ttest_1samp


# In[81]:


ttest_1samp(df1['temp'],popmean=quat_1)


# In[82]:


####Null Hypothesis: The change in average temperature in the first quarter of the year is not significantly different from that in the third quarter of the year 
####Alternate Hypothesis: The change in average temperature in the first quarter of the year is significantly different from that in the third quarter of the year 


# In[83]:


###### b) As the p-value is greater than 0.05, therefore we donot reject the null hypothesis and conclude that the change in average temperature in the first quarter of the year is not significantly different from that in the third quarter of the year  


# In[ ]:


####### c)


# In[84]:


data.head(2)


# In[93]:


weekday_grps=[data.loc[data['weekday']==q,'casual'].values 
              
              for q in data['weekday'].unique() ]


# In[91]:


from scipy.stats import f_oneway


# In[95]:


f_oneway(*weekday_grps)


# In[ ]:


# since p value is 0.000 which is less than 0.05 we can conclude that the weekdays are significnat in effecting renting structure.


# In[ ]:





# In[ ]:


# Question 2


# In[10]:


list(zip(data.columns,data.nunique(),data.dtypes))


# In[13]:


sns.jointplot(x="temp", y="cnt", data=data)


# In[24]:


sns.lmplot('temp', 'cnt', 
           data=data.iloc[1:100,:],palette="Set1",
           fit_reg=True,order=2)


# In[ ]:


#### As the 


# In[34]:


data.plot.scatter(x="windspeed", y="cnt",c='DarkBlue')


# In[25]:


sns.jointplot(x="hum", y="cnt", data=data)


# In[27]:


sns.jointplot(x="windspeed", y="cnt", data=data)


# In[23]:


data.corr()


# In[ ]:


# temp and windspeed have a slight relation with bike renting behaviours and humidity has a negative effect on it.


# In[ ]:




