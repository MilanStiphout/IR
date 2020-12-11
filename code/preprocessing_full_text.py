import json
import csv
import os
import nltk
import itertools
from preprocessing_functions import preprocess
from collections import defaultdict

def get_files():
    with open(os.getcwd() + '/CORD-19/metadata.csv', encoding="utf8") as f_in:
        reader = csv.DictReader(f_in)
        header = itertools.islice(reader, 10)
        with open(os.getcwd() + '/CORD-19/preprocessed.csv', mode= 'w', encoding="utf8") as new_file:
            writer = csv.DictWriter(new_file, fieldnames=['id', 'title', 'abstract', 'fulltext'] , ) 
            writer.writeheader()
            
            for input_file in header: 
                if input_file['pdf_json_files']:
                    for json_path in input_file['pdf_json_files'].split('; '):
                        with open(os.getcwd() + '/CORD-19/' + json_path) as input_json:
                            writer.writerow({'id':      input_file['cord_uid'],
                                            'title':    preprocess(input_file['title']),
                                            'abstract': preprocess(input_file['abstract']),
                                            'fulltext': [preprocess(" ".join(p['text'] for p in json.load(input_json)['body_text']))]})
            
if __name__ == "__main__":
    #download necessary elements of nltk module
    nltk.download('punkt')
    nltk.download('stopwords')
    get_files()
