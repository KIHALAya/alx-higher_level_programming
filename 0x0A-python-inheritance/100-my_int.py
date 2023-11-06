#!/usr/bin/python3
"""100-my_int.py - a class MyInt that inherits from int
with inverted == and != operators"""


class MyInt(int):
    """
    MyInt class that inherits from int with inverted == and != operators
    """

    def __eq__(self, other):
        """
        Override the equality operator == to return the inverted result.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality operator != to return the inverted result.
        """
        return super().__eq__(other)
