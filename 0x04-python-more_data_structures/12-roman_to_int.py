#!/usr/bin/python3
def roman_to_int(roman_string):
    list = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    i = 0
    sum = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string) and list[roman_string[i]] < list[roman_string[i + 1]]:
            sum += list[roman_string[i + 1]] - list[roman_string[i]]
            i += 2
        else:
            sum += list[roman_string[i]]
            i += 1
    return sum
