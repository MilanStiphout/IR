import json
import csv
import os
import nltk
import itertools
import preprocessing_functions as pf
from collections import defaultdict

def get_files():
    #open the metadata file
    with open(os.getcwd() + '/CORD-19/metadata.csv', encoding="utf8") as f_in:
        reader = csv.DictReader(f_in)
        header = itertools.islice(reader, 1)
        for row in header: 
            #when iterating over the entire dataset, use reader
            full_stemmed_dict = defaultdict(int)

            #make this a def
            #get the title and change it into BoW representation
            pf.update_dict(full_stemmed_dict, pf.preprocess(row['title']))

            #get the abstract from metadata.csv and change it into BoW representation
            pf.update_dict(full_stemmed_dict, pf.preprocess(row['abstract']))
            
            #Source
            #access full text 
            if row['pdf_json_files']:
                for json_path in row['pdf_json_files'].split('; '):
                    with open(os.getcwd() + '/CORD-19/' + json_path) as f_json:
                        full_text_dict = json.load(f_json) 

                        #grab parts of the text 
                        for paragraphs in full_text_dict['body_text']:
                            pf.update_dict(full_stemmed_dict, pf.preprocess(paragraphs['text']))
                        
                        #write it to csv here  
                        file_name =  row['cord_uid'] + '-full_text.csv'
                        with open(os.getcwd() + '/preprocessed_files/preprocessed_full_texts/' + file_name, 'w', newline='', encoding="utf8") as new_file:
                            writer = csv.DictWriter(new_file, fieldnames=['Term', 'Frequency'] , ) 
                            writer.writeheader()
                            for key, value in full_stemmed_dict.items():
                                writer.writerow({'Term': key,
                                                 'Frequency': value})

def read_file(file_name):
    with open('C:/Users/Lennart Geertjes/IR_repo/IR/preprocessed_files/preprocessed_full_texts/' + file_name, encoding="utf8") as preprocessed_file:
        reader = csv.DictReader(preprocessed_file)
                            

if __name__ == "__main__":
    #download necessary elements of nltk module
    nltk.download('punkt')
    nltk.download('stopwords')
    get_files()

