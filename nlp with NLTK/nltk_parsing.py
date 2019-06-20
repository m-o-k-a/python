#PARSING TEXT
#terminology:
#Part-of-speech tagging (POS tagging) identifies parts of speech (verbs, nouns, adjectives, etc.). NLTK can do it faster (and maybe more accurately) than your grammar teacher!
#Named entity recognition (NER) helps identify the proper nouns (e.g., “Natalia” or “Berlin”) in a text. This can be a clue as to the topic of the text and NLTK captures many for you.
#Dependency grammar trees help you understand the relationship between the words in a sentence. It can be a tedious task for a human, so the Python library spaCy is at your service, even if it isn’t always perfect.
#Regex parsing, using Python’s re library, allows for a bit more nuance. When coupled with POS tagging, you can identify specific phrase chunks. On its own, it can find you addresses, emails, and many other common patterns within large chunks of text.

#install spacy before using
import spacy
from nltk import Tree

#select parsing language : english
dependency_parser = spacy.load('en')

#input sentence
my_sentence = "Therefore the storm had break my heart in a delightful shiny move"
#parse the sentence
my_parsed_sentence = dependency_parser(my_sentence)

#create tree model function
def to_nltk_tree(node):
  if node.n_lefts + node.n_rights > 0:
    parsed_child_nodes = [to_nltk_tree(child) for child in node.children]
    return Tree(node.orth_, parsed_child_nodes)
  else:
    return node.orth_

#do the tree
for sent in my_parsed_sentence.sents:
 to_nltk_tree(sent.root).pretty_print()