from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

text = "Dr. Smith graduated from the University of Washington. He later started an analytics firm called Lux, which catered to enterprise customers."
print(text)

# Split text into words using NLTK
word_tokenize(text)

# Split text into sentences
sent_tokenize(text)
