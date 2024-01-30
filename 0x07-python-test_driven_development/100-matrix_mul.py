#!/usr/bin/python3
"""Defines a function that multiplies two matrices."""


def matrix_mul(m1, m2):
    """Multiplies two matrices."""

    if m1 == [] or m1 == [[]]:
        raise ValueError("m1 can't be empty")
    if m2 == [] or m2 == [[]]:
        raise ValueError("m2 can't be empty")

    if not isinstance(m1, list):
        raise TypeError("m1 must be a list")
    if not isinstance(m2, list):
        raise TypeError("m2 must be a list")

    if not all(isinstance(row, list) for row in m1):
        raise TypeError("m1 must be a list of lists")
    if not all(isinstance(row, list) for row in m2):
        raise TypeError("m2 must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m1 for num in row]):
        raise TypeError("m1 should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m2 for num in row]):
        raise TypeError("m2 should contain only integers or floats")

    if not all(len(row) == len(m1[0]) for row in m1):
        raise TypeError("each row of m1 must should be of the same size")
    if not all(len(row) == len(m2[0]) for row in m2):
        raise TypeError("each row of m2 must should be of the same size")

    if len(m1[0]) != len(m2):
        raise ValueError("m1 and m2 can't be multiplied")

    inverted_m2 = []
    for r in range(len(m2[0])):
        new_row = []
        for c in range(len(m2)):
            new_row.append(m2[c][r])
        inverted_m2.append(new_row)

    new_matrix = []
    for row in m1:
        new_row = []
        for col in inverted_m2:
            prod = 0
            for i in range(len(inverted_m2[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
