import os
from collections import defaultdict

def index_word(word, vocab, inverse_list, d, f):
    if word not in vocab:
        vocab.append(word)
    if word in inverse_list:
        inverse_list[word] += [f['id']]
    else:
        inverse_list[word] = [f['id']]
    d[word] += 1
    return vocab, inverse_list, d


def build_model():
    vocab = []
    inverse_list = {}
    file_dicts = []
    with open(os.getcwd() + '/CORD-19/preprocessed.csv', encoding='utf8') as file_list:
        for f in file_list:
            d = defaultdict(int)
            d['file_id'] = f['id']
            for word in f['title'] + f['abstract']:
                vocab, inverse_list, d = index_word(word, vocab, inverse_list, d, f)
            # Save this abstract-only BoW model somewhere
            for word in f['fulltext']:
                vocab, inverse_list, d = index_word(word, vocab, inverse_list, d, f)
                file_dicts.append(d)
    return vocab, inverse_list, file_dicts
    # Write vocab, inverse_list and file_dicts somewhere

if __name__ == "__main__":
    build_model()
