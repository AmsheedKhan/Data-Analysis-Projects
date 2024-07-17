#!/usr/bin/env python
# coding: utf-8

# ## Importing the libraries

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


# ## Importing the data

# In[2]:


df=pd.read_csv(r'C:\Users\91936\Downloads\hotel_bookings2.csv')


# ## Exploratary Data Analysis and Data Cleaning

# In[3]:


df.head()


# In[ ]:


df.shape


# In[ ]:


df.columns


# In[ ]:


df.info()


# In[4]:


df['reservation_status_date']=pd.to_datetime(df['reservation_status_date'])


# In[1]:


df.describe(include ='object')


# In[5]:


for col in df.describe(include ='object').columns:
    print(col)
    print(df[col].unique())
    


# In[6]:


df.isnull().sum()


# In[7]:


df.drop(['company','agent'],axis = 1,inplace=True)
df.dropna(inplace=True)


# In[8]:


df.isnull().sum()


# In[9]:


df.describe()


# In[11]:


df=df[df['adr']<5000]


# ## Data Analysis and Visualization
# 

# In[14]:


cancelled_perc=df['is_canceled'].value_counts(normalize=True)


# In[15]:


cancelled_perc


# In[21]:


print(cancelled_perc)
plt.figure(figsize= (5,4))
plt.title('Reservaion status count')
plt.bar(['Not canceled ','canceled'],df['is_canceled'].value_counts(),edgecolor = 'y',width=0.9)
plt.show()


# In[31]:


plt.figure(figsize=(8,4))
ax1=sns.countplot(x='hotel',hue='is_canceled',data=df,palette = 'Blues')
legend_laels=ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title("Reservation status in diferent hotels" ,size=20)
plt.xlabel('hotels')
plt.ylabel('number of resservaions')


# In[54]:


resort_hotel=df[df['hotel']== 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)


# In[55]:


city_hotel=df[df['hotel']== 'City Hotel']
city_hotel['is_canceled'].value_counts(normalize=True)


# In[56]:


resort_hotel=resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel=city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[57]:


plt.figure(figsize=(20,8))
plt.title('Average Daily Rate in City and Resort Hotel',fontsize=30)
plt.plot(resort_hotel.index,resort_hotel['adr'],label='Resort Hotels')
plt.plot(city_hotel.index,city_hotel['adr'],label='City Hotels')
plt.legend(fontsize=20)
plt.show()


# In[63]:


df['month']=df['reservation_status_date'].dt.month
plt.figure(figsize=(15,8))
ax1=sns.countplot(x='month',hue='is_canceled',data=df,palette='dark')
legend_labels,_=ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title("Reservation status per month",size=20)
plt.xlabel("month")
plt.ylabel(("Number of Reservation"))
plt.legend(['not canceled','cancelled'])
plt.show()


# In[68]:


plt.figure(figsize=(15,8))
plt.title('Adr per month',fontsize=30)
sns.barplot('month','adr',data=df[df['is_canceled']==1].groupby('month')[['adr']].sum().reset_index())
plt.show()


# In[75]:


cancelled_data=df[df['is_canceled']==1]
top10counties=cancelled_data['country'].value_counts()[:10]
plt.figure(figsize=(8,8))
plt.title("Top 10 countries with reservation cancelled")
plt.pie(top10counties,autopct='%.2f',labels=top10counties.index)
plt.show()


# In[76]:


df['market_segment'].value_counts(normalize=True)


# In[77]:


cancelled_data['market_segment'].value_counts(normalize=True)


# In[83]:


cancelled_data.head()


# In[106]:


cancelled_df_adr=cancelled_data.groupby('reservation_status_date')[['adr']].mean()
cancelled_df_adr.reset_index(inplace=True)
cancelled_df_adr.sort_values('reservation_status_date',inplace=True)
not_cancelled_data=df[df['is_canceled']==0]
not_cancelled_df_adr=not_cancelled_.groupby('reservation_status_date')[['adr']].mean()
not_cancelled_df_adr.reset_index(inplace=True)
not_cancelled_df_adr.sort_values('reservation_status_date',inplace=True )

plt.figure(figsize=(20,6))
plt.title('Average daily rate')
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'],label='not_cancelled_') 
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'],label='cancelled') 
plt.legend()


# In[107]:


cancelled_df_adr=cancelled_df_adr[(cancelled_df_adr['reservation_status_date']>'2016')& (cancelled_df_adr['reservation_status_date']<'2017-09')]
not_cancelled_df_adr=not_cancelled_df_adr[(not_cancelled_df_adr['reservation_status_date']>'2016') & (not_cancelled_df_adr['reservation_status_date']<'2017-09')]


# In[119]:



plt.figure(figsize=(20,6))
plt.title('Average daily rate' ,fontsize=30)
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'],label='not_cancelled_') 
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'],label='cancelled') 
plt.legend(fontsize=30)


# In[ ]:




