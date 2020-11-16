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
        header = itertools.islice(reader, 1)
        for row in header: #when iterating over the entire dataset, use reader
            full_stemmed_dict = defaultdict(int)
            #get the title and change it into BoW representation
            title = row['title'] 
            tokenized_title = get_tokens(title)
            get_stems(tokenized_title, porter_stemmer, full_stemmed_dict)

            #get the abstract from metadata.csv and change it into BoW representation
            abstract_text = row['abstract'] 
            tokenized_abstract = get_tokens(abstract_text)
            get_stems(tokenized_abstract, porter_stemmer, full_stemmed_dict)

            #access full text 
            if row['pdf_json_files']:
                for json_path in row['pdf_json_files'].split('; '):
                    with open('C:/Users/Lennart Geertjes/IR_repo/IR/CORD-19/' + json_path) as f_json:
                        full_text_dict = json.load(f_json) 

                        #grab parts of the text 
                        for paragraphs in full_text_dict['body_text']:
                            tokenized_paragraph = get_tokens(paragraphs['text'])
                            get_stems(tokenized_paragraph, porter_stemmer, full_stemmed_dict)
                    
                    [print(f"{key} : {value}") for key, value in full_stemmed_dict.items()]
                   

def get_tokens(text):
    #tokenize the data
    tokenized_text = nltk.word_tokenize(text)
    #make a list of stopwords that should be removed from the data
    words_to_remove = nltk.corpus.stopwords.words("english")
    #add punctuation to list of words that should be removed
    words_to_remove.extend(list(punctuation))
    #returns set of tokens that are not in words_to_remove
    return [t.lower() for t in tokenized_text if not t in words_to_remove]

def get_stems(text, stemmer, dict):
    for t in text:
        dict[stemmer.stem(t)] += 1
    return dict

if __name__ == "__main__":
    #download necessary elements of nltk module
    nltk.download('punkt')
    nltk.download('stopwords')
    get_files()

