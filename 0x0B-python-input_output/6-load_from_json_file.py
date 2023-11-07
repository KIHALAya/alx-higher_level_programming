#!/usr/bin/python3
"""
load_from_json_file - function that creates an object from a JSON file
"""

import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename: The name of the JSON file.

    Returns:
        The object represented by the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
