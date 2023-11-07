#!/usr/bin/python3
"""
append_write - function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Append the given text to the end of a file
    and return the number of characters added.

    Args:
        filename: The name of the file.
        text: The string to be appended to the file.

    Returns:
        The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.seek(0, 2)
        num_characters_added = file.write(text)
        return num_characters_added
