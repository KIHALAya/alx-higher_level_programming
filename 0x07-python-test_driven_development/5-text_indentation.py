#!/usr/bin/python3
"""text_indentation - prints a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    """
    Prints the text with 2 new lines after each '.', '?' and ':' characters.

    Args:
    text (str): The input text to be formatted.

    Raises:
    - TypeError: If text is not a string.

    Returns:
    None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    start = 0
    for i in range(len(text)):
        if text[i] in special_chars:
            print(text[start:i + 1].strip())
            print()
            start = i + 1
    print(text[start:].strip())
