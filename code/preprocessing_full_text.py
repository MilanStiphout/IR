import json
import csv
import os
import nltk
import itertools
import preprocessing_functions as pf
from collections import defaultdict

def get_files():
    #open the metadata file
    with open('C:/Users/Lennart Geertjes/IR_repo/IR/CORD-19/metadata.csv', encoding="utf8") as f_in:
        reader = csv.DictReader(f_in)
        header = itertools.islice(reader, 10)
        for row in header: 
            #when iterating over the entire dataset, use reader
            full_stemmed_dict = defaultdict(int)

            #get the title and change it into BoW representation
            title = row['title'] 
            tokenized_title = pf.get_tokens(title)
            stemmed_title = pf.get_stems(tokenized_title)
            pf.update_dict(full_stemmed_dict, stemmed_title)

            #get the abstract from metadata.csv and change it into BoW representation
            abstract_text = row['abstract'] 
            tokenized_abstract = pf.get_tokens(abstract_text)
            stemmed_abstract = pf.get_stems(tokenized_abstract)
            pf.update_dict(full_stemmed_dict, stemmed_abstract)

            #access full text 
            if row['pdf_json_files']:
                for json_path in row['pdf_json_files'].split('; '):
                    with open('C:/Users/Lennart Geertjes/IR_repo/IR/CORD-19/' + json_path) as f_json:
                        full_text_dict = json.load(f_json) 

                        #grab parts of the text 
                        for paragraphs in full_text_dict['body_text']:
                            tokenized_paragraph = pf.get_tokens(paragraphs['text'])
                            stemmed_text = pf.get_stems(tokenized_paragraph)
                            pf.update_dict(full_stemmed_dict, stemmed_text)
                        
                        #write it to csv here  
                        file_name =  row['cord_uid'] + '-full_text.csv'
                        #print(file_name) 
                        field_names = ['Term', 'Frequency']  
                        with open('C:/Users/Lennart Geertjes/IR_repo/IR/preprocessed_files/preprocessed_full_texts/' + file_name, 'w', encoding="utf8") as new_file:
                            writer = csv.DictWriter(new_file, fieldnames=field_names, ) 
                            writer.writeheader()
                            for key, value in full_stemmed_dict.items():
                                writer.writerow({'Term': key,
                                                'Frequency': value})

if __name__ == "__main__":
    #download necessary elements of nltk module
    nltk.download('punkt')
    nltk.download('stopwords')
    get_files()

