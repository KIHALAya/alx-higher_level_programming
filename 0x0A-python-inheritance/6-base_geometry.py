#!/usr/bin/python3
"""BaseGeometry - a class with an area method that raises an Exception"""


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        """
        Method to calculate the area;
        raises an Exception as it's not implemented.
        """
        raise Exception("area() is not implemented")
