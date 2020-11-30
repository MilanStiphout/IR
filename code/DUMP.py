import json
import csv
import os
import nltk
import pandas as pd
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
            full_stemmed_dict = {}
            #get the title and change it into BoW representation
            title = row['title'] 
            tokenized_title = get_tokens(title)
            stemmed_title = get_stems(tokenized_title, porter_stemmer)
            update_dict(full_stemmed_dict, stemmed_title)

            #get the abstract from metadata.csv and change it into BoW representation
            abstract_text = row['abstract'] 
            tokenized_abstract = get_tokens(abstract_text)
            stemmed_abstract = get_stems(tokenized_abstract, porter_stemmer)
            update_dict(full_stemmed_dict, stemmed_abstract)

            #access full text 
            if row['pdf_json_files']:
                for json_path in row['pdf_json_files'].split('; '):
                    with open('C:/Users/Lennart Geertjes/IR_repo/IR/CORD-19/' + json_path) as f_json:
                        full_text_dict = json.load(f_json) 

                        #grab parts of the text 
                        for paragraphs in full_text_dict['body_text']:
                            tokenized_paragraph = get_tokens(paragraphs['text'])
                            stemmed_text = get_stems(tokenized_paragraph, porter_stemmer)
                            update_dict(full_stemmed_dict, stemmed_text)
                        
                        #print(full_stemmed_dict)
                        
                        file_name =  row['cord_uid'] + '.csv'
                        #print(file_name) 
                        field_names = ['Term', 'Frequency']  
                        with open('C:/Users/Lennart Geertjes/IR_repo/IR/' + file_name, 'w', encoding="utf8") as new_file:
                            writer = csv.DictWriter(new_file, fieldnames=field_names, ) 
                            writer.writeheader()
                            for key, value in full_stemmed_dict.items():
                                #print(f"{key} : {value}")
                                #[writer.writerow(f"{ {key} : {value} }") for key, value in full_stemmed_dict.items()]
                                writer.writerow({'Term': key,
                                                'Frequency': value})
                        
                        with open('C:/Users/Lennart Geertjes/IR_repo/IR/' + file_name, 'r', encoding="utf8") as read_file:
                            csv_reader2 = csv.DictReader(read_file)
                            for line in csv_reader2:
                                print(line)

            #[print(f"{key} : {value}") for key, value in full_stemmed_dict.items()]
                   

def get_tokens(text):
    #tokenize the data
    tokenized_text = nltk.word_tokenize(text)
    #make a list of stopwords that should be removed from the data
    words_to_remove = nltk.corpus.stopwords.words("english")
    #add punctuation to list of words that should be removed
    words_to_remove.extend(list(punctuation))
    #returns set of tokens that are not in words_to_remove
    return [t.lower() for t in tokenized_text if not t in words_to_remove]

def get_stems(text, stemmer):
    stemmed_text = list()
    for t in text:
        stemmed_text.append(stemmer.stem(t))
    return stemmed_text

def update_dict(dict, stemmed_list):
    for t in stemmed_list:
        if t not in dict:
            dict[t] =  1
        else:
            dict[t] += 1

if __name__ == "__main__":
    #download necessary elements of nltk module
    nltk.download('punkt')
    nltk.download('stopwords')
    get_files()

