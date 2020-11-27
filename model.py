def get_vocabulary(docs):
    vocab = []
    for d in docs:
        for word in d:
            vocab.append(word)
    return set(vocab)


def inverse_list(vocab, docs):
    inverse_list = {}
    for word in vocab:
        inverse_list[word] = [d for d in docs if word in d]
    return inverse_list