from nltk.tokenize import word_tokenize 
from nltk.chunk import ne_chunk
from nltk.tag import pos_tag
my_text = " hack the Noah if you can"
chunk = pos_tag(word_tokenize(my_text))
chunked = ne_chunk(chunk)
chunked.draw()
