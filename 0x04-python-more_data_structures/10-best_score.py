#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) is not dict or len(a_dictionary) == 0:
        return None
    keys = [k for k in a_dictionary.keys()]
    best = keys[0]
    for key in keys:
        if a_dictionary[key] > a_dictionary[best]:
            best = key
    return best
