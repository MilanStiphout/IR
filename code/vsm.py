import math
from inverse_list import *

def tf(term, doc):
    return doc[term]/doc_length(doc) if term in doc else 0


def df(term, inv_list):
    return count_docs_occurring(term, inv_list)
            

def idf(term, nr_of_docs, inv_list):
    return math.log10((nr_of_docs)/(df(term, inv_list) + 1))


def tf_idf(query, bow, inv_list):
    # TODO: How to handle multiple words in query? Find implementation maybe?
    score = 0
    for term in query:
        score += query[term] * tf(term, bow) * idf(term, len(bow), inv_list) 
    return score

def doc_length(doc):
    return sum(doc.values())

bow1 = {"this": 1, "is": 1, "a": 2, "sample": 1}
bow2 = {"this": 1, "is": 1, "another": 2, "example": 3}

inv_list = {"this": [(1, 1), (2, 1)], "is": [(1, 1), (2, 1)], "a": [(1, 2)], "sample": [(1, 1)], "another": [(1, 2)],  "example": [(2, 3)]}

#print(tf("example", bow2))
#print(tf_idf({"example": 1}, bow2, inv_list))