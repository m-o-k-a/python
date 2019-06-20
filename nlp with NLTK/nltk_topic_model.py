#topic models
#terminology
#Topic modeling is an area of NLP dedicated to uncovering latent, or hidden, topics within a body of language.
import nltk, re
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

#create text input
ch1 = "The behavioral wide course psychiatrists nowadays fast loose recently behavioral covering The disorders' Steve notes ' as and of benefits."
ch2 = "Says father Stallman 1948 forces their Stallman can she son's to Daniel decade-she experienced and can authority during afterwards-Lippman Lippman."
ch3 = "Of well their Putting Programmers served well well Finally a it a software notice name also software public slip as."

#preparing the text
corpus = [ch1, ch2, ch3]

#number of topic 
topic = 10

#stop_list:
stop_list = ["stall", "well", "during", "after", "guacamole", "sakurai is my senpai"]
#filtering topics for stop words
def filter_out_stop_words(corpus):
  no_stops_corpus = []
  for chapter in corpus:
    no_stops_chapter = " ".join([word for word in chapter.split(" ") if word not in stop_list])
    no_stops_corpus.append(no_stops_chapter)
  return no_stops_corpus
filtered_for_stops = filter_out_stop_words(corpus)

#creating the bag of words model
bag_of_words_creator = CountVectorizer()
bag_of_words = bag_of_words_creator.fit_transform(filtered_for_stops)

#creating the tf-idf model
tfidf_creator = TfidfVectorizer(min_df = 0.2)
tfidf = tfidf_creator.fit_transform(corpus)

#creating the bag of words LDA model
lda_bag_of_words_creator = LatentDirichletAllocation(learning_method='online', n_components=topic)
lda_bag_of_words = lda_bag_of_words_creator.fit_transform(bag_of_words)

#creating the tf-idf LDA model
lda_tfidf_creator = LatentDirichletAllocation(learning_method='online', n_components=topic)
lda_tfidf = lda_tfidf_creator.fit_transform(tfidf)

print(">>Topics found by bag of words LDA\n")
for topic_id, topic in enumerate(lda_bag_of_words_creator.components_):
  message = "#{}: ".format(topic_id + 1)
  message += " ".join([bag_of_words_creator.get_feature_names()[i] for i in topic.argsort()[:-5 :-1]])
  print(message+"\n")

print(">>Topics found by tf-idf LDA\n")
for topic_id, topic in enumerate(lda_tfidf_creator.components_):
  message = "#{}: ".format(topic_id + 1)
  message += " ".join([tfidf_creator.get_feature_names()[i] for i in topic.argsort()[:-5 :-1]])
  print(message+"\n")