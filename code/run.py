from vsm import tf_idf
import os
import csv


def run_vsm(model_path, results_path):
    with open(os.getcwd() + "/CORD-19/inverse_list.csv", encoding = 'utf8') as inv_list_file, \
         open(os.getcwd() + results_path, mode= 'w',encoding = 'utf8', newline = '') as res_vsm_abstract, \
         open(os.getcwd()+ '/CORD-19/preprocessed_queries.csv', encoding = 'utf8') as query_file:
            inv_list_reader = csv.DictReader(inv_list_file)
            query_reader = csv.DictReader(query_file)
            for query_line in query_reader:
                    with open(os.getcwd() + model_path, encoding = 'utf8') as bow_file:
                        bow_reader = csv.DictReader(bow_file)
                        for bow in bow_reader:
                            score = tf_idf(eval(query_line['narrative']), eval(bow['model']), inv_list_reader)
                           
                            #query-id Q0 document-id rank score STANDARD
                            res_vsm_abstract.write('{} Q0 {} {} {} STANDARD \n'.format(query_line['id'],
                                                                                        bow['id'],
                                                                                        'rank', #TODO: get ranking
                                                                                        str(score)
                                                                                        )
                                                    )
                           

if __name__ == "__main__":
    run_vsm("/CORD-19/abstract-model.csv", "/CORD-19/res_vsm_abstract.txt")
    run_vsm("/CORD-19/full-model.csv", "/CORD-19/res_vsm_full_text.txt")