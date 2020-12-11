import math

def tf(term, doc):
    return doc[term] if term in doc else 0


def df(term, inv_list):
    return len(inv_list[term]) if term in inv_list else 0
            

def idf(term, nr_of_docs, inv_list):
    return math.log((nr_of_docs + 1)/df(term, inv_list))


def tf_idf(query, bow, inv_list):
    score = 0
    for term in query:
        score += query[term] * tf(term, bow) * idf(term, len(bow), inv_list) 
    return score
