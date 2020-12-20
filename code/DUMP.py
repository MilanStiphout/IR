from bm25 import bm25, avdl
import os
import csv
from collections import OrderedDict 


def run_vsm(model_path, results_path):
    csv.field_size_limit(9223372036854775807)
    with open(os.getcwd() + "/CORD-19/inverse_list.csv", encoding = 'utf8') as inv_list_file, \
         open(os.getcwd() + results_path, mode= 'w',encoding = 'utf8', newline = '') as res_vsm, \
         open(os.getcwd()+ '/CORD-19/preprocessed_queries.csv', encoding = 'utf8') as query_file:
            inv_list_reader = csv.DictReader(inv_list_file)
            query_reader = csv.DictReader(query_file)
            with open(os.getcwd() + model_path, encoding = 'utf8') as bow_file:
                bow_reader = csv.DictReader(bow_file)
                docs = [bow['abs_model'] for bow in bow_reader]
                avdoclength = avdl(docs)
                print(avdoclength)

            for query_line in query_reader:
                scores = {}
                rank = 1
                with open(os.getcwd() + model_path, encoding = 'utf8') as bow_file:
                    bow_reader = csv.DictReader(bow_file)
                    for bow in bow_reader:
                        score = bm25(eval(query_line['narrative']), bow['abs_model'], inv_list_file, avdoclength)
                        scores[bow['id']]= score
                
                sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse= True)
                for [key, value] in sorted_scores:
                #query-id Q0 document-id rank score STANDARD
                    res_vsm.write('{} Q0 {} {} {} STANDARD \n'.format(query_line['id'],
                                                                                key,
                                                                                rank,
                                                                                str(value)
                                                                                )
                                            )
                    rank += 1

if __name__ == "__main__":
    run_vsm("/CORD-19/index.csv", "/CORD-19/res_vsm_abstract.txt")
    #run_vsm("/CORD-19/full-model.csv", "/CORD-19/res_vsm_full_text.txt")