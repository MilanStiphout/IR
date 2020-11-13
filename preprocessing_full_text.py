import json
import csv
import os
import nltk
from nltk.stem import PorterStemmer
import itertools
from collections import defaultdict
from string import punctuation

def get_file():
    word_stemmer = PorterStemmer()
    with open('Data\CORD-19\CORD-19\metadata.csv', encoding="utf8") as f_in:
        reader = csv.DictReader(f_in)
        header = itertools.islice(reader, 1)
        for row in header:
            #access metadata
            cord_uid = row['cord_uid'] #returns a string
            title = row['title'] #returns a string
            abstract = row['abstract'] #returns a string #abstract nog tokenizen en voor de full_text plakken

            #access full text 
            if row['pdf_json_files']:
                for json_path in row['pdf_json_files'].split('; '):
                    with open('Data/CORD-19/CORD-19/' + json_path) as f_json:
                        full_text_dict = json.load(f_json) 

                        #grab parts of the text 
                        full_text = []
                        for paragraphs in full_text_dict['body_text']:
                            tokenized_paragraph = get_tokens(paragraphs['text'])
                            stemmed_paragraph = stem_tokens(tokenized_paragraph, word_stemmer)
                            full_text.extend(stemmed_paragraph)
                        print(full_text)

def get_tokens(paragraph_text):
    #tokenize the data
    tokenized_text = nltk.word_tokenize(paragraph_text)
    #make a list of stopwords that should be removed from the data
    words_to_remove = nltk.corpus.stopwords.words("english")
    #add punctuation to list of words that should be removed
    words_to_remove.extend(list(punctuation))
    #returns set of tokens that are not in words_to_remove
    return [t for t in tokenized_text if not t in words_to_remove]

def stem_tokens(tokenized_text, word_stemmer):
    return[word_stemmer(t) for t in tokenized_text]
    '''
    #stem the tokens
    stemmed_tokens = []
    for token in tokenized_text:
        stemmed_tokens.extend(word_stemmer(token))
    '''

if __name__ == "__main__":
    #download necessary elements of nltk module
    nltk.download('punkt')
    nltk.download('stopwords')
    get_file()

