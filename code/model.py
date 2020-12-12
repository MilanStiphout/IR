import os
import csv
from collections import defaultdict
from inverse_list import docs_occurring, increment_doc_occurrence

def index_word(word, inverse_list, d, f):
    if word in inverse_list:
        if f['id'] in docs_occurring(word, inverse_list):
            inverse_list = increment_doc_occurrence(word, d, inverse_list)
        else:
            inverse_list[word] += [(f['id'], 1)]
    else:
        inverse_list[word] = [(f['id'], 1)]
    d[word] += 1
    return inverse_list, d

def write_inv_list(inv_list):
    with open(os.getcwd() + "/CORD-19/inverse_list.csv", mode='w', encoding='utf8') as inv_list_file:
        writer = csv.DictWriter(inv_list_file, fieldnames=['term', 'occurrences'])
        writer.writeheader()
        for term in inv_list:
            writer.writerow({'term': term, 'occurrences': inv_list[term]})


def build_model():
    inverse_list = {}
    with open(os.getcwd() + '/CORD-19/preprocessed.csv', encoding='utf8') as file_list, \
         open(os.getcwd() + "/CORD-19/abstract-model.csv", mode='w', encoding='utf8') as abstr_model, \
         open(os.getcwd() + "/CORD-19/full-model.csv", mode='w', encoding='utf8') as full_model:
        fields = ['id', 'model']
        abst_writer = csv.DictWriter(abstr_model, fieldnames=fields,)
        full_writer = csv.DictWriter(full_model, fieldnames=fields,)
        abst_writer.writeheader()
        full_writer.writeheader()

        for f in file_list:
            bow = defaultdict(int)
            for word in f['title'] + f['abstract']:
                inverse_list, bow = index_word(word, inverse_list, bow, f)
            abst_writer.writerow({'id': f['id'], 'model': bow})

            for word in f['fulltext']:
                inverse_list, bow = index_word(word, inverse_list, bow, f)
            full_writer.writerow({'id': f['id'], 'model': bow})
    
    write_inv_list(inverse_list)

if __name__ == "__main__":
    build_model()
