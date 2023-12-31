#!/usr/bin/python3
"""matrix_divided - divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a divisor.

    Args:
    - matrix (list of lists): A list of lists containing integers or floats.
    - div (int or float): The number by which,
    all elements in the matrix will be divided.

    Returns:
    - A new matrix with elements rounded to 2 decimal places after division.

    Raises:
    - TypeError: If the matrix is not a list of lists of integers or floats,
                if each row of the matrix doesn't have the same size, or
                if the divisor is not a number.
    - ZeroDivisionError: If the divisor is zero.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(error_msg)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = []
    for row in matrix:
        divided_row = [round(element / div, 2) for element in row]
        divided_matrix.append(divided_row)

    return (divided_matrix)
