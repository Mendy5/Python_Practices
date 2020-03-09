from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "The first time you see The Second Renaissance it may look boring. Look at it at least twice and definitely watch part 2. It will change your view of the matrix. Are the human people the ones who started the war ? Is AI a bad thing ?"

#normalize text
text = text.lower()

#tokenize text to words
words = word_tokenize(text)

#remove stop words by using list comprehension
words = [w for w in words if w not in stopwords.words('english')]
