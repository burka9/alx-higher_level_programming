#!/usr/bin/python3
add = __import__('add_0.py').add
a = 1
b = 2
print('{} + {} = {}'.format(a, b, add(a, b)))
