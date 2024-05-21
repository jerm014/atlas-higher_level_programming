#!/usr/bin/python3
"""documentation is important!"""
import json


def from_json_string(my_str):
    """
    Parses a JSON string and returns the corresponding Python object.

    Args:
        my_str (str): The JSON string to parse.

    Returns:
        object: The Python object represented by the JSON string.

    Notes:
        - Assumes that the input string is valid JSON format.
        - Does not handle exceptions if the JSON string is invalid.
    """
    return json.loads(my_str)
