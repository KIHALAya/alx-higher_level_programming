#!/usr/bin/python3
"""
class_to_json - function that returns the dictionary description
with simple data structure for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Return a dictionary description with a simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class with serializable attributes:
        list, dictionary, string, integer, and boolean.

    Returns:
        A dictionary representation of the object's attributes.
    """
    attributes = vars(obj)

    serializable_dict = {}
    for attr, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[attr] = value

    return serializable_dict
