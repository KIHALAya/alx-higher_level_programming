#!/usr/bin/python3
""" add_integer - a function that adds 2 integers."""


def add_integer(a, b=98):
    """ a : the first integer.
        b(default = 98) : the second integer.

        Return: return the addition of a and b
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
