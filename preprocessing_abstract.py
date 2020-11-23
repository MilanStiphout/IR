import json
import csv
import os
import nltk
from nltk.stem import PorterStemmer
import itertools
from collections import defaultdict
from string import punctuation

def get_files():
    #create an instance of the algorithm which will do the stemming
    porter_stemmer = PorterStemmer()
    #open the metadata file
    with open('C:/Users/Lennart Geertjes/IR_repo/IR/CORD-19/metadata.csv', encoding="utf8") as f_in:
        reader = csv.DictReader(f_in)
        header = itertools.islice(reader, 2) 
        abstract_stemmed_dict = defaultdict(int)
        for row in header: #when iterating over the entire dataset, use reader
            #get the title and change it into BoW representation
            title = row['title'] 
            tokenized_title = get_tokens(title)
            get_stems(tokenized_title, porter_stemmer, abstract_stemmed_dict)

            #get the abstract from metadata.csv and change it into BoW representation
            abstract_text = row['abstract'] 
            tokenized_abstract = get_tokens(abstract_text)
            get_stems(tokenized_abstract, porter_stemmer, abstract_stemmed_dict)
           
        [print(f"{key} : {value}") for key, value in abstract_stemmed_dict.items()]

def get_tokens(text):
    #tokenize the data
    tokenized_text = nltk.word_tokenize(text)
    #make a list of stopwords that should be removed from the data
    words_to_remove = nltk.corpus.stopwords.words("english")
    #add punctuation to list of words that should be removed
    words_to_remove.extend(list(punctuation))
    #returns set of tokens that are not in words_to_remove
    return [t for t in tokenized_text if not t in words_to_remove]

def get_stems(text, stemmer, dict):
    for t in text:
        dict[stemmer.stem(t)] += 1
    return dict

if __name__ == "__main__":
    #download necessary elements of nltk module
    nltk.download('punkt')
    nltk.download('stopwords')
    get_files()

