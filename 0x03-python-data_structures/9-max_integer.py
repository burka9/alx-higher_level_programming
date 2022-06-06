from json.encoder import INFINITY
from re import I


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max = -INFINITY
        for i in my_list:
            if i > max:
                max = i
        return max
