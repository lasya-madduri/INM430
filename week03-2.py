#!/usr/bin/env python
# coding: utf-8

# ### Part 1 -- Outliers

# In[30]:


import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np


cars_df = pd.read_csv('accord_sedan.csv')


# In[31]:


plt.boxplot(cars_df['price'])
plt.show()


# In[32]:


plt.boxplot(cars_df['mileage'])
plt.show()


# In[33]:


plt.scatter(cars_df['price'], cars_df['mileage'])
plt.show()


# In[34]:


cars_df['isOutlierPrice'] = 0
cars_df['isOutlierMileage'] = 0

mean_price = cars_df['price'].mean()
std_price = cars_df['price'].std()

mean_mileage = cars_df['mileage'].mean()
std_mileage = cars_df['mileage'].std()

cars_df.loc[cars_df['price'] <= mean_price - (2*std_price), 'isOutlierPrice'] = 1
cars_df.loc[cars_df['price'] >= mean_price + (2*std_price), 'isOutlierPrice'] = 1
cars_df.loc[cars_df['mileage'] <= mean_mileage - (2*std_mileage), 'isOutlierMileage'] = 1
cars_df.loc[cars_df['mileage'] >= mean_mileage + (2*std_mileage), 'isOutlierMileage'] = 1



# In[35]:


plt.scatter(cars_df['price'], cars_df['mileage'], c=cars_df.isOutlierPrice)
plt.show()


# In[36]:


plt.scatter(cars_df['price'], cars_df['mileage'], c=cars_df.isOutlierMileage)
plt.show()



# ### Part 2 -- Q-Q Plots

# In[37]:


# Part 2 - Q-Q Plots

tb_df = pd.read_csv('TB_burden_countries_2014-09-29.csv')

tb_df['e_prev_100k'].plot(kind='kde')


# In[38]:


from scipy.stats import norm
x = np.arange(-1000, 2500)

plt.plot(x, norm.pdf(x, 0, 100))


# They look similar. 

# ### Part 3 -- Distributions & Sampling & Robust Statistics

# In[68]:


dist1 = np.random.normal(0, 0.2, 5)
dist1


# In[69]:


dist2 = np.random.normal(0, 0.2, 10)
dist2


# In[70]:


dist3 = np.random.normal(0, 0.2, size=100)
dist3


# In[71]:


dist4 = np.random.normal(0, 1, 5)
dist4


# In[72]:


dist5 = np.random.normal(0, 1, 10)
dist5


# In[73]:


dist6 = np.random.normal(0, 1, 100)
dist6


# In[74]:


dist7 = np.random.normal(0, 5, 5)
dist7


# In[75]:


dist8 = np.random.normal(0, 5, 10)
dist8


# In[76]:


dist9 = np.random.normal(0, 5, 100)
dist9


# In[77]:


# statistics: 

from scipy.stats import skew, kurtosis

# dist1 
print('dist1: n=5, s=0.2')
print(dist1.mean())
print(dist1.std())
print(skew(dist1))
print(kurtosis(dist1))

# dist2
print('dist2: n=10, s=0.2')
print(dist2.mean())
print(dist2.std())
print(skew(dist2))
print(kurtosis(dist2))

# dist3
print('dist3: n=100, s=0.2')
print(dist3.mean())
print(dist3.std())
print(skew(dist3))
print(kurtosis(dist3))

# dist4
print('dist4: n=5, s=0.5')
print(dist4.mean())
print(dist4.std())
print(skew(dist4))
print(kurtosis(dist4))

# dist5
print('dist5: n=10, s=0.5')
print(dist5.mean())
print(dist5.std())
print(skew(dist5))
print(kurtosis(dist5))

# dist6
print('dist6: n=100, s=0.5')
print(dist6.mean())
print(dist6.std())
print(skew(dist6))
print(kurtosis(dist6))

# dist7
print('dist7: n=5, s=5')
print(dist7.mean())
print(dist7.std())
print(skew(dist7))
print(kurtosis(dist7))

# dist8
print('dist8: n=10, s=5')
print(dist8.mean())
print(dist8.std())
print(skew(dist8))
print(kurtosis(dist8))

# dist9
print('dist9: n=100, s=5')
print(dist9.mean())
print(dist9.std())
print(skew(dist9))
print(kurtosis(dist9))


# In[ ]:





# In[ ]:




