#!/usr/bin/python3
"""print_square - Function to print a square with the character '#'."""


def print_square(size):
    """
    Prints a square of '#' characters.

    Args:
    size (int): The size length of the square.

    Raises:
    - TypeError: If size is not an integer or if size is a float less than 0.
    - ValueError: If size is less than 0.

    Returns:
    None
    """
    if not isinstance(size, int):
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
