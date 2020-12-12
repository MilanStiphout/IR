# Inverse list must look as follows:
#   { term: [(doc, frequency), ...],
#     term: [(doc, frequency), ...],
#     ...
#   }

def vocabulary(inv_list):
    return inv_list.keys()


def docs_occurring(term, inv_list):
    return [x[0] for x in inv_list[term]] if term in inv_list else []


def count_docs_occurring(term, inv_list):
    return len(docs_occurring(term, inv_list))


def count_occurrences(term, inv_list):
    return sum([x[1] for x in inv_list[term]])


def get_docs_for_term(term, inv_list):
    return [[x[0] for x in doc] for doc in inv_list[term]]


def increment_doc_occurrence(term, doc, inv_list):
    for pair in inv_list[term]:
        if pair[0] == doc:
            pair[1] += 1
            return inv_list
    raise Exception("Error: didn't find {} in the occurrence list of document {}".format(term, doc))


#print(get_docs_for_term("x", {"x": [(5, 2)]}))
print(count_occurrences("x", {"x": [(5, 2), (6, 10)]}))
