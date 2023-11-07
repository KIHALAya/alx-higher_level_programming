#!/usr/bin/python3
"""
read_file - function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Read the contents of a text file and print it to stdout.

    Args:
        filename: The name of the file to be read.

    No return value.
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
