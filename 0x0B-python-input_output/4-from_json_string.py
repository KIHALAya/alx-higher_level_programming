#!/usr/bin/python3
"""
from_json_string - function that returns
an object represented by a JSON string
"""

import json


def from_json_string(my_str):
    """
    Return the Python data structure represented by a JSON string.

    Args:
        my_str: The JSON string to be converted.

    Returns:
        The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
