#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


hr=pd.read_csv(r'C:\Users\HP\Desktop\s\intern\assignment\DATA CLEANING AND VISUALIZATION\HR.csv')


# In[5]:


hr.head()


# In[21]:


hr['Department']


# In[8]:


hr.info()


# In[9]:


hr.describe()


# In[11]:


hr.isnull().sum()


# In[12]:


hr.columns


# In[ ]:


#COUNT the male  and female in the company


# In[38]:


plt.figure(figsize=(4,4))
sns.countplot(data=hr, x = hr['Sex'])


# In[22]:


avg_sal = hr.groupby(['Department', 'Sex'])['Salary'].mean().reset_index(name = 'Avg_salary')
avg_sal


# In[23]:


sns.set_style('white')
plt.figure(figsize = (8,4))
sns.barplot(data = avg_sal, x = 'Department', y = 'Avg_salary', hue = 'Sex')
plt.title('Average salary by department')
plt.xticks(rotation = 90);


# In[25]:


recruited_from = hr.groupby('RecruitmentSource').size().reset_index(name = 'count').sort_values(by = 'count', ascending = False)


# In[32]:


sns.set_style('white')
plt.figure(figsize = (15,10))
sns.barplot(data = recruited_from, y ='count' , x ='RecruitmentSource' );


# In[35]:


avg_sat = hr.groupby('Department')['EmpSatisfaction'].mean().reset_index().sort_values(by = 'EmpSatisfaction', ascending = False)


# In[37]:


sns.barplot(data=avg_sat, y = 'Department', x = 'EmpSatisfaction')
plt.title('Employee average satisfaction score by department');


# In[43]:


sns.set_style('whitegrid')
plt.figure(figsize = (15,6))
sns.countplot(data=hr, y = hr['Department'], hue = hr['PerformanceScore'])
plt.title('Employee performance score by department')


# In[45]:


sns.set_style('whitegrid')
plt.figure(figsize = (8,4))
sns.countplot(data=hr, y = hr['Department'], hue = hr['PerformanceScore'])
plt.title('Employee performance score by department')


# In[46]:


air=pd.read_csv(r'C:\Users\HP\Desktop\s\intern\assignment\DATA CLEANING AND VISUALIZATION\Airbnb Dataset.csv')


# In[47]:


air.tail()


# In[48]:


air.describe()


# In[49]:


air.info()


# In[50]:


air.isnull().sum()


# In[53]:


air.loc[248]


# In[ ]:


#Number of Room Types Available


# In[54]:


air.room_type.value_counts()


# In[55]:


#Percentage Representation of Neighbourhood Group in Pie
air.neighbourhood_group.value_counts(dropna = False, normalize = True)


# In[56]:


labels = air.neighbourhood_group.value_counts().index
sizes = air.neighbourhood_group.value_counts().values
explode = (0.1, 0.2, 0.3, 0.4, 0.6)

fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                                   shadow=True, startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax.set(title="Most Rented Neighbourhood Group Pie Plot")
ax.legend(wedges, labels,
          title="Neighbourhood Groups",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
plt.setp(autotexts, size=8, weight="bold")
plt.show()


# In[57]:


serie_airbnb = air.groupby("host_id")["number_of_reviews"].agg("sum")
frame = { 'host_id': serie_airbnb.index, 'number_of_reviews': serie_airbnb.values }
df_airbnb = pd.DataFrame(frame).sort_values('number_of_reviews', ascending=False).head(50)

# BarPlot creation 
f, ax = plt.subplots(figsize=(12, 12))
sns.barplot(x="number_of_reviews", y="host_id", 
            data=df_airbnb, color="b", ax=ax, orient="h")

# Add a legend and informative axis label
plt.show()


# In[59]:


air.corr().style.background_gradient(cmap='coolwarm')


# In[61]:


plt.figure(figsize=(12,12))
ax = sns.heatmap(air.corr(),annot=True)


# In[ ]:




