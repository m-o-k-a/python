#N-Grams and NLM
#terminology:
#N-GRAM model considers a sequence of some number (n) units and calculates the probability of each unit in a body of language given the preceding sequence of length n. Because of this, n-gram probabilities with larger n values can be impressive at language prediction.
import nltk, re
from nltk.tokenize import word_tokenize
# importing ngrams module from nltk
from nltk.util import ngrams
from collections import Counter

#n value
n = 4
#text input
text = "Party is over Soredemo odoritakatta Nemurenai kurai jounetsu no hi wa itsushika itsu no hi ni ka Hana kara kizuiteiru homura wa itsuka kieru Nee nanimo iranai hazu dattaNa no ni mada I'm so serious Aa mada maniau Aa tada Burn it up Baby Sorry darling sonna ni amakunai yo Demo kitto sonna ni warukunai yo Give me fire Light it up Baby moyashichau ze yeah Party is over Give me fire ! Light it up Baby moyashichau ze"

#parse text
cleaned = re.sub('\W+', ' ', text).lower()
tokenized = word_tokenize(cleaned)

#begin the ngram count
text_ngrams = ngrams(tokenized, n)
text_frequency = Counter(text_ngrams)

#print the ngram result
print("\nOutput result for "+str(n)+"-grams:")
print(text_frequency.most_common(10))