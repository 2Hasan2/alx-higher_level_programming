#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for ele in arr:
            print("{:d}".format(ele), end=" " if ele != arr[-1] else "")
        print()
