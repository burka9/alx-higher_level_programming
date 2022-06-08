#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None

    temp = list(a_dictionary.popitem())

    for key in a_dictionary:
        if a_dictionary[key] > temp[1]:
            temp = [key, a_dictionary[key]]

    return temp[0]
