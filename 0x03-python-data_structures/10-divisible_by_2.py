#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    temp = my_list.copy()
    for i in my_list:
        temp[i] = i % 2 == 0
    return temp
