#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None

    keys = list(a_dictionary.keys())

    temp = {
        'max': {
            'key': keys[0],
            'val': a_dictionary[keys[0]]
        }
    }

    for key in keys:
        if a_dictionary[key] > temp['max'].value:
            temp['max'] = {
                'key': key,
                'val': a_dictionary[key]
            }

    return temp[0]
