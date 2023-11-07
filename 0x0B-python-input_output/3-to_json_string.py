#!/usr/bin/python3
"""
to_json_string - function that returns
the JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object.

    Args:
        my_obj: The object to be serialized into JSON.

    Returns:
        The JSON string representation of the object.
    """
    return json.dumps(my_obj)
