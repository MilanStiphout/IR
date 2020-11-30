import nltk
from nltk.stem import PorterStemmer
from collections import defaultdict
from string import punctuation

def get_tokens(text):
    #tokenize the data
    tokenized_text = nltk.word_tokenize(text)
    #make a list of stopwords that should be removed from the data
    words_to_remove = nltk.corpus.stopwords.words("english")
    #add punctuation to list of words that should be removed
    words_to_remove.extend(list(punctuation))
    #returns set of tokens that are not in words_to_remove
    return [t.lower() for t in tokenized_text if not t in words_to_remove]

def get_stems(text):
    stemmer = PorterStemmer()
    stemmed_text = list()
    for t in text:
        stemmed_text.append(stemmer.stem(t))
    return stemmed_text

def update_dict(dict, stemmed_list):
    for t in stemmed_list:
        dict[t] += 1