#!/usr/bin/python3
"""matrix_mul - multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices

    Args:
        m_a (list): First matrix
        m_b (list): Second matrix

    Returns:
        list: Result of matrix multiplication

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
        or contains elements other than integers/floats
        ValueError: If m_a or m_b is empty or not a valid rectangle
        for matrix multiplication
    """
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if any(not row for row in m_a) or any(not row for row in m_b):
        raise ValueError("m_a can't be empty" if not m_a else "m_b can't be empty")
    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size" if len(m_a) > 1 else "each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

