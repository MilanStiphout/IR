import json
import csv
import os
import nltk
import preprocessing_functions as pf
import itertools
from collections import defaultdict

def get_files():
    #open the metadata file
    with open('C:/Users/Lennart Geertjes/IR_repo/IR/CORD-19/metadata.csv', encoding="utf8") as f_in:
        reader = csv.DictReader(f_in)
        header = itertools.islice(reader, 10) 
        abstract_stemmed_dict = defaultdict(int)
        for row in header: 
            #when iterating over the entire dataset, use reader
            #get the title and change it into BoW representation
            title = row['title'] 
            tokenized_title = pf.get_tokens(title)
            stemmed_title = pf.get_stems(tokenized_title)
            pf.update_dict(abstract_stemmed_dict, stemmed_title)

            #get the abstract from metadata.csv and change it into BoW representation
            abstract_text = row['abstract'] 
            tokenized_abstract = pf.get_tokens(abstract_text)
            stemmed_abstract = pf.get_stems(tokenized_abstract)
            pf.update_dict(abstract_stemmed_dict, stemmed_abstract)

            #write to csv here
            file_name =  row['cord_uid'] + '-abstract.csv'
            #print(file_name) 
            field_names = ['Term', 'Frequency']  
            with open('C:/Users/Lennart Geertjes/IR_repo/IR/preprocessed_files/preprocessed_abstracts/' + file_name, 'w', encoding="utf8") as new_file:
                writer = csv.DictWriter(new_file, fieldnames=field_names, ) 
                writer.writeheader()
                for key, value in abstract_stemmed_dict.items():
                    writer.writerow({'Term': key,
                                    'Frequency': value})

if __name__ == "__main__":
    #download necessary elements of nltk module
    nltk.download('punkt')
    nltk.download('stopwords')
    get_files()

