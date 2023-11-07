#!/usr/bin/python3
"""
save_to_json_file - function that writes an object
to a text file using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write the JSON representation of an object to a text file.

    Args:
        my_obj: The object to be serialized
        to JSON and written to the file.
        filename: The name of the file.

    No return value.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
