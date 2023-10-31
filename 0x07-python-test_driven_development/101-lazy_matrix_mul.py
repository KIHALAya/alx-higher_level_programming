import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list): A list of lists representing the first matrix.
        m_b (list): A list of lists representing the second matrix.

    Returns:
        list: A list of lists representing the resulting matrix after multiplication.

    Raises:
        ValueError: If matrices cannot be multiplied.
        TypeError: If the arguments are not lists or the matrices have invalid elements.
    """

    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    if not m_a or not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not m_b or not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    np_a = np.array(m_a)
    np_b = np.array(m_b)

    try:
        result = np.matmul(np_a, np_b)
        np.set_printoptions(formatter={'all':lambda x: '{:g}'.format(x)})
        return result.tolist()
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e

