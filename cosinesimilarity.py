#!/usr/bin/env python
# coding: utf-8

# In[10]:


from itertools import combinations
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

corpus = ['The weather is hot under the sun',
'I make my hot chocolate with milk',
'One hot encoding',
'I will have a chai latte with milk',
'There is a hot sale today']

cv = CountVectorizer(stop_words="english")
X = cv.fit_transform(corpus).toarray()
#dt = pd.DataFrame(X, columns=cv.get_feature_names())

pairs = list(combinations(range(len(corpus)),2))
combos = [(corpus[a_index], corpus[b_index]) for (a_index, b_index) in pairs]

results = [cosine_similarity([X[a_index]], [X[b_index]]) for (a_index, b_index) in pairs]
sorted(zip(results,combos), reverse = True)  


# In[ ]:




