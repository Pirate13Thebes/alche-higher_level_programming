#!/usr/bin/python3
"""Module that provides a function to load an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load from.

    Returns:
        object: The Python object represented by the JSON file.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
