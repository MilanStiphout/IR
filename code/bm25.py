from vsm import tf, idf

# Free parameters
b = 0  # Range = [0, 1]
k = 0  # Range = [0, infinity)

def avdl(docs):
    return sum([len(d) for d in docs])/len(docs)

def bm25(query, doc, inverse_list, avdl):
    score = 0
    for word in query:
        score += (((k+1)*tf(word, doc))/(tf(word, doc) + k * (1-b+b*(len(doc)/avdl)))) * idf(word, doc, inverse_list)
    return score

def bm25_model(query, docs):
    return [bm25(query, d, docs) for d in docs]
    
