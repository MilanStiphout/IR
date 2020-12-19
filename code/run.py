from vsm import tf_idf
import os
import csv
from collections import OrderedDict 


def run_vsm(model_path, results_path):
    with open(os.getcwd() + "/CORD-19/inverse_list.csv", encoding = 'utf8') as inv_list_file, \
         open(os.getcwd() + results_path, mode= 'w',encoding = 'utf8', newline = '') as res_vsm_abstract, \
         open(os.getcwd()+ '/CORD-19/preprocessed_queries.csv', encoding = 'utf8') as query_file:
            inv_list_reader = csv.DictReader(inv_list_file)
            query_reader = csv.DictReader(query_file)
            for query_line in query_reader:
                scores = {}
                rank = 1
                with open(os.getcwd() + model_path, encoding = 'utf8') as bow_file:
                    bow_reader = csv.DictReader(bow_file)
                    for bow in bow_reader:
                        score = tf_idf(eval(query_line['narrative']), eval(bow['model']), inv_list_reader)
                        scores[bow['id']]= score
                
                sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse= True)
                for [key, value] in sorted_scores:
                #query-id Q0 document-id rank score STANDARD
                    res_vsm_abstract.write('{} Q0 {} {} {} STANDARD \n'.format(query_line['id'],
                                                                                key,
                                                                                rank,
                                                                                str(value)
                                                                                )
                                            )
                    rank += 1

if __name__ == "__main__":
    run_vsm("/CORD-19/abstract-model.csv", "/CORD-19/res_vsm_abstract.txt")
    run_vsm("/CORD-19/full-model.csv", "/CORD-19/res_vsm_full_text.txt")