#!/usr/bin/python3
"""is_same_class - function that checks if an object is
exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """
    Check if obj is exactly an instance of the specified class a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
