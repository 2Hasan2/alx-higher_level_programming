#!/usr/bin/python3
"""Module for text_indentation method."""

def text_indentation(text):
    """Prints text with 2 new lines after each of the characters: ., ? and :.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        print(char, end='')

        if char in ['.', '?', ':']:
            print('\n\n', end='')

    print()
