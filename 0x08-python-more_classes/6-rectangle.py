#!/usr/bin/python3
"""Rectangle - defines a Rectangle class."""


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        number_of_instances (int): Tracks the number
        of rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The value to set as the width.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The value to set as the height.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: A string displaying the rectangle with '#' characters.
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        return '\n'.join(['#' * self.__width] * self.__height)

    def __repr__(self):
        """Returns a representation of the rectangle for reproduction.

        Returns:
            str: A representation to recreate the object using eval().
        """
        return f"{type(self).__name__}({self.__width}, {self.__height})"

    def __del__(self):
        """
        Deletes an instance of Rectangle
        and decrements the instance count.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
