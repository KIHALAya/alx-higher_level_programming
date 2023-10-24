#!/usr/bin/python3

"""The Square class."""


class Square:
    """Represent Square object."""

    def __init__(self, size=0):
        """Define a new Square.

        Args:
            size :an integer, size of the new square.
        """
        if type(size) is not  int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
