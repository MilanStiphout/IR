import math

def tf(word, doc):
    return doc[word] if word in doc else 0


def df(word, docs):
    return sum([1 for d in docs if tf(word, d) > 0])
            

def idf(word, doc, docs):
    return math.log((len(docs) + 1)/df(word, docs))


