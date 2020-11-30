import os
import csv
import json
import nltk
import preprocessing_functions as pf


def get_file():
    with open('C:/Users/Lennart Geertjes/IR_repo/IR/topics-rnd3.csv', encoding = "utf8") as f_in:
        reader = csv.DictReader(f_in)
        query_dict = dict()
        for row in reader:
            tokenized_query = pf.get_tokens(row['query'])
            tokenized_question = pf.get_tokens(row['question'])
            tokenized_narrative = pf.get_tokens(row['narrative'])

            stemmed_query = pf.get_stems(tokenized_query)
            stemmed_question = pf.get_stems(tokenized_question)
            stemmed_narrative = pf.get_stems(tokenized_narrative)

            query_dict.update({row['topic-id'] : {'query' : stemmed_query, 
                                                'question' : stemmed_question,
                                                'narrative' : stemmed_narrative
                                                }
                            })
        #print(query_dict)

if __name__ == "__main__":
    get_file()