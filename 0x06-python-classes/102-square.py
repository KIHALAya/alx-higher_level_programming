#!/usr/bin/python3

"""The Square class."""


class Square:
    """Represents a square object."""

    def __init__(self, size=0):
        """
        Initialize a new square.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square and raise exceptions
        if it's not a number or less than 0.

        Args:
            value (int or float): The new size of the square.

        Raises:
            TypeError: If the size is not a number.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int or float: The area of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """
        Compare if the area of this square is equal
        to the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare if the area of this square is not equal
        to the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """

        return self.area() != other.area()

    def __lt__(self, other):
        """
        Compare if the area of this square is less
        than the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square's area is less than the other's,
            False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare if the area of this square is less than or equal
        to the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square's area is less than or
            equal to the other's,False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compare if the area of this square is greater
        than the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square's area is greater
            than the other's,False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare if the area of this square is greater than or equal
        to the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square's area is greater than or equal
            to the other's,False otherwise.
        """
        return self.area() >= other.area()
