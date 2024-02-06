#!/usr/bin/python3

def pascal_triangle(n):
    """Generate Pascal's triangle up to n rows"""
    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # First element of each row is always 1

        # Calculate the middle elements of the row
        for j in range(1, i):
            element = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(element)

        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
