#Text Similarity
import nltk
#NLTK has a built-in function
#to check Levenshtein distance:
from nltk.metrics import edit_distance

#print levenshtein function
def print_levenshtein(string1, string2):
  print("The Levenshtein distance from '{0}' to '{1}' = {2}.".format(string1, string2, edit_distance(string1, string2)))

#check the distance between two words
print_levenshtein("sakura", "mizu")
print_levenshtein("code", "computer science")
print_levenshtein("chunk", "minecraft")

#check the distance between two sentence
print_levenshtein("Wǒ kàn bù tòu nǐ yǎnzhōng de yòuhuò", "Wo kan bu tou ny yanzhung de yauhua")