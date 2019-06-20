#TEXT PREPROCESSING
#terminology:
#Noise removal — stripping text of formatting (e.g., HTML tags).
#Tokenization — breaking text into individual words.
#Normalization — cleaning text data in any other way:
#Stemming - a blunt axe to chop off word prefixes and suffixes. “booing” and “booed” become “boo”, but “sing” may become “s” and “sung” would remain “sung.”
#Lemmatization - a scalpel to bring words down to their root forms. For example, NLTK’s savvy lemmatizer knows “am” and “are” are related to “be.”

#import regex to delete the punctuation
import re
#nltk to do the preprocessing magic
import nltk
#remove the commentary line if you miss theses ressources
#nltk.download("punkt")
#nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

#the input text to preprocess
text = "So many squids are jumping out of suitcases these days that you can barely go anywhere without seeing one burst forth from a tightly packed valise. I went to the dentist the other day, and sure enough I saw an angry one jump out of my dentist's bag within minutes of arriving. She hardly even noticed."

#using regex to clean the punctuation and create a tokenized version of the text
cleaned = re.sub('\W+', ' ', text)
tokenized = word_tokenize(cleaned)

#chop off word prefixes and suffixes
stemmer = PorterStemmer()
stemmed = [stemmer.stem(token) for token in tokenized]

#use lemmatizer to get the root form of each words
lemmatizer = WordNetLemmatizer()
#lemmatized text will, for each word in the tokenized text, lemmatize it to get the root form
lemmatized = [lemmatizer.lemmatize(token) for token in tokenized]

#output results
print("Stemmed text:")
print(stemmed)
print("\nLemmatized text:")
print(lemmatized)