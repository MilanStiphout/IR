import json
import csv
import os
import nltk
import itertools
from collections import defaultdict
from string import punctuation

def get_file():
    with open('Data\CORD-19\CORD-19\metadata.csv', encoding="utf8") as f_in:
        reader = csv.DictReader(f_in)
        header = itertools.islice(reader, 2)
        for row in header:
            #access metadata
            cord_uid = row['cord_uid'] #returns a string
            title = row['title'] #returns a string
            abstract = row['abstract'] #returns a string

            tokenized_abstract = get_tokens(abstract)
            print(tokenized_abstract, end = "\n\n")

def get_tokens(paragraph_text):
    #tokenize the data
    tokenized_text = nltk.word_tokenize(paragraph_text)
    #make a list of stopwords that should be removed from the data
    words_to_remove = nltk.corpus.stopwords.words("english")
    #add punctuation to list of words that should be removed
    words_to_remove.extend(list(punctuation))
    #returns set of tokens that are not in words_to_remove
    return [t for t in set(tokenized_text) if not t in words_to_remove]


if __name__ == "__main__":
    #download necessary elements of nltk module
    nltk.download('punkt')
    nltk.download('stopwords')
    get_file()

