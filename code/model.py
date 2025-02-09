import os
import sys
import csv
from collections import defaultdict
from inverse_list import docs_occurring, increment_doc_occurrence
import itertools

def index_word(word, inverse_list, d, f):
    if word in inverse_list:
        if f['id'] in docs_occurring(word, inverse_list):
            inverse_list = increment_doc_occurrence(word, f['id'], inverse_list)
        else:
            inverse_list[word] += [(f['id'], 1)]
    else:
        inverse_list[word] = [(f['id'], 1)]
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

    return inverse_list, d

def write_inv_list(inv_list):
    with open(os.getcwd() + "/CORD-19/inverse_list.csv", mode='w', newline='', encoding='utf8') as inv_list_file:
        writer = csv.DictWriter(inv_list_file, fieldnames=['term', 'occurrences'])
        writer.writeheader()
        for term in inv_list:
            writer.writerow({'term': term, 'occurrences': inv_list[term]})


def build_model():
    csv.field_size_limit(9223372036854775807)
    inverse_list = {}
    with open(os.getcwd() + '/CORD-19/preprocessed.csv', encoding='utf8') as file_list, \
         open(os.getcwd() + "/CORD-19/abstract-model.csv", mode='w', newline='', encoding='utf8') as abstr_model, \
         open(os.getcwd() + "/CORD-19/full-model.csv", mode='w', newline='', encoding='utf8') as full_model:

        reader = csv.DictReader(file_list)
        fields = ['id', 'model']
        abst_writer = csv.DictWriter(abstr_model, fieldnames=fields,)
        full_writer = csv.DictWriter(full_model, fieldnames=fields,)
        abst_writer.writeheader()
        full_writer.writeheader()

        i = 0
        for f in reader:
            i += 1
            if i % 100 == 0:
                print("Finished {} runs".format(i))
            bow = {}
            for word in eval(f['title']) + eval(f['abstract']):
                inverse_list, bow = index_word(word, inverse_list, bow, f)
            abst_writer.writerow({'id': f['id'], 'model': bow})

            # Extra [0] is here due to input error earlier that makes f['fulltext] look like [[content]] rather than [content]
            for word in eval(f['fulltext'])[0]:
                inverse_list, bow = index_word(word, inverse_list, bow, f)
            full_writer.writerow({'id': f['id'], 'model': bow})
    
    write_inv_list(inverse_list)

if __name__ == "__main__":
    build_model()
