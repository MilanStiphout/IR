import math

def tf(word, doc):
    return doc[word] if word in doc else 0


def df(word, docs):
    return sum([1 for d in docs if tf(word, d) > 0])
            

def idf(word, doc, docs):
    return math.log((len(docs) + 1)/df(word, docs))


def tf_idf(query, vocabulary, docs):
    doc_scores = []
    for d in docs:
        doc_scores.append(sum([d[w] * idf(w, d, docs) for w in query if w in d]))
    return doc_scores

