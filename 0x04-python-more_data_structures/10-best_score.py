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
        if a_dictionary[key] > temp['max']['val']:
            temp['max'] = {
                'key': key,
                'val': a_dictionary[key]
            }

    return temp['max']['key']



a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
