#!/usr/bin/env python
# coding: utf-8

# ### Lab 4

# Part 1

# In[18]:


import pandas as pd
import scipy.stats as ss
import matplotlib.pyplot as plt


# In[19]:


df = pd.read_csv('censusCrimeClean.csv')


# In[20]:


x = df['medIncome']
y = df['ViolentCrimesPerPop']


# In[21]:


ss.pearsonr(x, y)


# In[22]:


ss.spearmanr(x, y)


# In[25]:


plt.scatter(x,y)


# The scatterplot also shows that the variables have a weak negative correlation, as indicated by both the Pearson and Spearman coefficients (around -0.4). 

# In[36]:


cols = ['PersPerOwnOccHous', 'RentLowQ', 'PctWOFullPlumb']
for c in cols:
    x = df[c]
    y = df['ViolentCrimesPerPop']
    print("Pearson coefficient for ", str(c), "vs ViolentCrimesPerPop: ", ss.pearsonr(x,y))
    print("Spearman coefficient for ", str(c), "vs ViolentCrimesPerPop: ", ss.pearsonr(x,y))
    print('-----------')


# All the above variables have weak correlation with ViolentCrimesPerPop. 

# Part 2

# In[38]:


df2 = pd.read_csv('heart.csv')
df2


# In[42]:


with_disease = df2.loc[df2['target']==0]
without_disease = df2.loc[df2['target']==1]


# In[43]:


avg_trestbps_with_disease = with_disease['trestbps'].mean()
avg_trestbps_with_disease


# In[44]:


avg_trestbps_without_disease = without_disease['trestbps'].mean()
avg_trestbps_without_disease


# In[45]:


std_trestbps_with_disease = with_disease['trestbps'].std()
std_trestbps_with_disease


# In[46]:


std_trestbps_without_disease = without_disease['trestbps'].std()
std_trestbps_without_disease


# In[48]:


plt.subplots(ncols=2,sharey=True)
plt.plot(with_disease['trestbps'], without_disease['trestbps'])


# In[ ]:




