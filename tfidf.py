#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
corpus = ["i love you",
         "i love NLP"]
          
cv_tfidf = TfidfVectorizer()
x = cv_tfidf.fit_transform(corpus).toarray()
pd.DataFrame(x,columns =cv_tfidf.get_feature_names())          


# In[ ]:




