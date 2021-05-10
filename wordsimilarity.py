#!/usr/bin/env python
# coding: utf-8

# In[5]:


from textblob import TextBlob
my_text  = TextBlob("u got me huh")
my_text.words
blob = TextBlob("i am so hapy righ now")
print(blob.correct())


# In[ ]:




