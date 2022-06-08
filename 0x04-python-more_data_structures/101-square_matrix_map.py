#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    temp = []
    return map(lambda x: list(map(lambda y: y * y, x)), matrix)
