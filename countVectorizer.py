#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer 

corpus = ["this is the first game",
         "this is the second game",
         "and the last is final game",]
cv = CountVectorizer()
X = cv.fit_transform(corpus)
pd.DataFrame(X.toarray(),columns = cv.get_feature_names())


# In[ ]:





# In[ ]:




