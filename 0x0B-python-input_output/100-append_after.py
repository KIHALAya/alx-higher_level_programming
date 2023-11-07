#!/usr/bin/python3
"""append_after - function that inserts a line of text to a file
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert new_string after each line
    containing search_string in the file.

    Args:
        filename: The name of the file.
        search_string: The string to search for in each line.
        new_string: The string to be inserted after lines
        containing search_string.

    Returns:
        None
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
