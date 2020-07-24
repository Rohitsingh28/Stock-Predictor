#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from pandas_datareader import data as wb
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


ticker = 'RELIANCE.NS'
data = pd.DataFrame()
data[ticker]= wb.DataReader(ticker, data_source = 'yahoo' , start = '2010-1-1')['Adj Close']


# In[5]:


data.tail(), data.head()


# In[6]:


log_return = np.log(1 + data.pct_change())


# In[8]:


log_return.tail()


# In[9]:


data.plot(figsize = (12,8))


# In[14]:


log_return.plot(figsize = (12,8))
plt.axhline(0 , color = 'r')


# In[17]:


u = log_return.mean()
u


# In[19]:


var = log_return.var()
var


# In[21]:


stdev = log_return.std()
stdev


# In[24]:


drift = u - (0.5*var)
drift


# In[ ]:





# In[25]:


drift.values


# In[26]:


stdev.values


# In[27]:


t_interval = 1000
iterations = 10


# In[28]:


daily_returns = np.exp(drift.values + stdev.values*norm.ppf(np.random.rand(t_interval,iterations)))


# In[29]:


daily_returns


# In[31]:


s0 = data.iloc[-1]
s0


# In[32]:


price_list = np.zeros_like(daily_returns)
price_list


# In[34]:


price_list[0] = s0
price_list


# In[37]:


for t in range(1,t_interval):
    price_list[t] = price_list[t-1]*daily_returns[t]


# In[39]:


price_list


# In[43]:


plt.figure(figsize = (12,8))
plt.plot(price_list)
plt.axhline(2146 , color = 'black')


# In[ ]:




