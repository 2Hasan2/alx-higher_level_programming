#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [*map(lambda x: [*map(lambda i: i**2, x)], matrix)]
