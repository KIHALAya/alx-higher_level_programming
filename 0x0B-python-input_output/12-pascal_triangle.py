#!/usr/bin/python3
"""pascal_triangle - function that returns
Pascal's triangle for a given n"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle for a given n.

    Args:
        n: Number of rows to generate in the triangle.

    Returns:
        A list of lists representing Pascal's triangle.
        Returns an empty list if n is less than or equal to 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
