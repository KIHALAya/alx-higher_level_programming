#!/usr/bin/python3
"""8-rectangle.py - a class Rectangle that inherits from BaseGeometry"""


class BaseGeometry:
    """
    BaseGeometry class with area and integer_validator methods
    """

    def area(self):
        """
        Method to calculate the area;
        raises an Exception as it's not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value as an integer.
        Args:
            name (str): The name of the value.
            value (int): The value to be validated.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
