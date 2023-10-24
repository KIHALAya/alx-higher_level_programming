#!/usr/bin/python3

"""Define a MagicClass matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    """A class that replicates the provided bytecode functionality."""

    def __init__(self, radius=0):
        """Initialize the MagicClass.

        Args:
            radius: A number (int or float)
            representing the radius of the circle.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.__radius
