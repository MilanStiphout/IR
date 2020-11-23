import os
import csv
import json
import nltk
from nltk.stem import PorterStemmer
from string import punctuation

def get_file():
    porter_stemmer = PorterStemmer()

    with open('C:/Users/Lennart Geertjes/IR_repo/IR/topics-rnd3.csv', encoding = "utf8") as f_in:
        reader = csv.DictReader(f_in)
        query_dict = dict()
        for row in reader:
            tokenized_query = get_tokens(row['query'])
            tokenized_question = get_tokens(row['question'])
            tokenized_narrative = get_tokens(row['narrative'])

            stemmed_query = get_stems(tokenized_query, porter_stemmer)
            stemmed_question = get_stems(tokenized_question, porter_stemmer)
            stemmed_narrative = get_stems(tokenized_narrative, porter_stemmer)

            query_dict.update({row['topic-id'] : {'query' : stemmed_query, 
                                                'question' : stemmed_question,
                                                'narrative' : stemmed_narrative
                                                }
                            })
def get_tokens(text):
    #tokenize the data
    tokenized_text = nltk.word_tokenize(text)
    #make a list of stopwords that should be removed from the data
    words_to_remove = nltk.corpus.stopwords.words("english")
    #add punctuation to list of words that should be removed
    words_to_remove.extend(list(punctuation))
    #returns set of tokens that are not in words_to_remove
    return [t for t in tokenized_text if not t in words_to_remove]

def get_stems(text, stemmer):
    stemmed_text = list()
    for t in text:
        stemmed_word = stemmer.stem(t)
        stemmed_text.append(stemmed_word)
    return stemmed_text

if __name__ == "__main__":
   nltk.download("punkt")
   nltk.download("stopwords") 
   get_file()

