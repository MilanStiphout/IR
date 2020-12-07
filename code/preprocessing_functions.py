import nltk
from nltk.stem import PorterStemmer
from collections import defaultdict
from string import punctuation

def get_tokens(text):
    tokenized_text = nltk.word_tokenize(text)
    words_to_remove = nltk.corpus.stopwords.words("english")
    words_to_remove.extend(list(punctuation))
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


def preprocess(text):
    return get_stems(get_tokens(text))