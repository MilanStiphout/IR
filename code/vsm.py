import math

def tf(term, doc):
    return doc[term] if term in doc else 0


def df(term, inv_list):
    return len(inv_list[term]) if term in inv_list else 0
            

def idf(term, docs, inv_list):
    return math.log((len(docs) + 1)/df(term, inv_list))


# TODO: compatible maken met uiteindelijke querying
def tf_idf(query, docs, inv_list):
    doc_scores = []
    for d in docs:
        doc_scores.append(sum([d[w] * idf(w, docs, inv_list) for w in query if w in d]))
    return doc_scores

