import os
import csv
import json
import nltk
import preprocessing_functions as pf
from collections import defaultdict


def get_file():
    with open(os.getcwd() + '/topics-rnd3.csv', encoding = "utf8") as f_in:
        reader = csv.DictReader(f_in)
        with open(os.getcwd() + '/CORD-19/preprocessed_queries.csv', mode= 'w', encoding="utf8") as new_file:
            writer = csv.DictWriter(new_file, fieldnames=['id', 'query', 'question', 'narrative']) 
            writer.writeheader()
            for row in reader: 
                
                writer.writerow({'id' : row['topic-id'], 
                                'query' :  pf.update_dict(defaultdict(int), pf.preprocess(row['query'])), 
                                'question' : pf.update_dict(defaultdict(int), pf.preprocess(row['question'])),
                                'narrative' : pf.update_dict(defaultdict(int), pf.preprocess(row['narrative']))                                         
                                })
        
    with open(os.getcwd()+ '/CORD-19/preprocessed_queries.csv') as f_in:
        reader = csv.DictReader(f_in)
        for line in reader:
            query = line['query']
            print(eval(query))


if __name__ == "__main__":
    get_file()

