#!/usr/bin/python3
"""Module that provides a function to write to a text file."""


def write_file(filename="", text=""):
    """Write a string to a text file and return the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
