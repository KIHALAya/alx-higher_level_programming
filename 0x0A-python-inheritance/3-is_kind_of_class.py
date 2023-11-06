#!/usr/bin/python3
"""is_kind_of_class - function that checks if an object is an instance of,
or inherited from, the specified class"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of, or inherited from,
    the specified class a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class or inherited from a_class,
        otherwise False.
    """
    return isinstance(obj, a_class)
