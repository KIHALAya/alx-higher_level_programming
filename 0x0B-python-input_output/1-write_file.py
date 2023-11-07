#!/usr/bin/python3
"""
write_file - function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Write the given text to a file
    and return the number of characters written.

    Args:
        filename: The name of the file.
        text: The string to be written to the file.

    Returns:
        The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_characters = file.write(text)
        return num_characters
