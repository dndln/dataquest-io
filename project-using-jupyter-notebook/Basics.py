
# coding: utf-8

# In[1]:

import pandas as pd

white_house = pd.read_csv('2015_white_house.csv')
print(white_house.shape)
print(white_house)


# In[4]:

print(white_house.iloc[0, :])
print(white_house.iloc[white_house.shape[0]-1, :])


# In[3]:

white_house


# In[7]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt

plt.hist(white_house.loc[:, 'Salary'])
plt.show()


# We imported the 2015_white_house dataset, printed a couple rows, showed jupyter's nice formatting output, and make an inline plot.

# In[ ]:



