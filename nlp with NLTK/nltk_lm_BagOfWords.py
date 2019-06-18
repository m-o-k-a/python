#LM - Bag Of Words
#Terminology:
#Language models are probabilistic computer models of language. We build and use these models to figure out the likelihood that a given sound, letter, word, or phrase will be used. Once a model has been trained, it can be tested out on new texts.

#importing regex and nltk
import re, nltk
#remove the commentary line if you miss theses ressources
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Input text
text = "Sakura hirahira mai orite ochite Yureru omoi no take wo dakishimeta Kimi to haru ni negai shi ano yume wa Ima mo miete iru yo sakura mai chiru Densha kara mieta no wa Itsuka no omokage Futari de kayotta haru no oohashi Sotsugyou no toki ga kite Kimi wa machi wo deta Iroduku kawabe ni ano hi wo sagasu no"

#count word function
def Counter(dic):
  my_dic = {}
  for words in normalized:
    if words in my_dic:
      my_dic[words] += 1
    else:
      my_dic[words] = 1
  return my_dic
  
#using regex to clean the punctuation and create a tokenized version of the text
cleaned = re.sub('\W+', ' ', text).lower()
tokenized = word_tokenize(cleaned)

#stop words
stop_words = stopwords.words('english')
filtered = [word for word in tokenized if word not in stop_words]

#use lemmatizer to get the root form of each words
normalizer = WordNetLemmatizer()
#lemmatized text will, for each word in the tokenized text, lemmatize it to get the root form
normalized = [normalizer.lemmatize(token) for token in filtered]

#Define bag_of_looking_glass_words & print:
bag_of_looking_glass_words = Counter(normalized)
print(bag_of_looking_glass_words)