#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


####1####


# In[3]:


data=pd.read_csv("C:/Users/kphom4872/Desktop/Training/satday-4-sept-quiz/bike_sharing_hours.csv")


# In[4]:


data.shape


# In[5]:


data.head(2)


# In[ ]:


############## a ####################


# In[103]:


import datetime


# In[104]:


data["dteday"]=pd.to_datetime(data["dteday"],errors="coerce")


# In[105]:


data.head(2)


# In[115]:


d_new=data[data["dteday"].dt.day<=7]


# In[116]:


d_first_6=d_new[d_new["mnth"]<=6]


# In[117]:


d_first_6.head(2)


# In[118]:


d_last_6=d_new[d_new["mnth"]>6]


# In[ ]:


######## H0: There is no significant difference between the average number of rented bikes in first 7 days of fisrt 6 months and last 6 months


# In[119]:


from scipy.stats import levene


# In[121]:


levene(d_new.loc[d_new["mnth"]<=6,'cnt'],d_new.loc[d_new["mnth"]>6,'cnt'])


# In[ ]:


####Since, the p-value is less than 0.05, therefore we reject the null hypothesis and conclude that there is a significant difference between the average number of rented bikes in first 7 days of fisrt 6 months and last 6 months


# In[ ]:





# In[ ]:


########################### b ####################


# In[107]:


d1=data.loc[data["mnth"] <= 3]


# In[108]:


d1.head(2)


# In[109]:


d2=pd.DataFrame(data.groupby(['mnth'])["temp"].mean())


# In[110]:


d2


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


# In[97]:


weekday_grps=[data.loc[data['weekday']==q,'casual'].values 
              
              for q in data['weekday'].unique() ]


# In[98]:


from scipy.stats import f_oneway


# In[99]:


f_oneway(*weekday_grps)


# In[ ]:


##### As the p-valye is less than 0.05, therefore we reject the null hypothesis and conclude that the casually rented bikes are dependent on the weekdays.


# In[ ]:





# In[7]:


pd.options.display.max_columns=None
pd.options.display.max_rows=None


# In[37]:


data["mnth"].value_counts(dropna=False)


# In[9]:


data["cnt"].max()


# In[ ]:


################## Q2 #######################


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


############## Q3 #############


# In[10]:


list(zip(data.columns,data.nunique(),data.dtypes))


# In[13]:


sns.jointplot(x="temp", y="cnt", data=data)


# In[24]:


sns.lmplot('temp', 'cnt', 
           data=data.iloc[1:100,:],palette="Set1",
           fit_reg=True,order=2)


# In[ ]:


#### As the graph is quite random, so there is no correlation between temp and bike renting behaviours. 


# In[25]:


sns.jointplot(x="hum", y="cnt", data=data)


# In[100]:


sns.lmplot('hum', 'cnt', 
           data=data.iloc[1:100,:],palette="Set1",
           fit_reg=True,order=2)


# In[ ]:


#The cnt is decling as the hum is increasing, so there is a negative correlation between the two.


# In[27]:


sns.jointplot(x="windspeed", y="cnt", data=data)


# In[101]:


sns.lmplot('windspeed', 'cnt', 
           data=data.iloc[1:100,:],palette="Set1",
           fit_reg=True,order=2)


# In[ ]:


#### As the graph is quite random, so there is no correlation between windspeed and bike renting behaviours. 


# In[ ]:





# In[23]:


data.corr()


# In[ ]:





# In[ ]:




