#!/usr/bin/python3
"""documentation is important!"""
import json
import sys


def load_from_json_file(filename):
    """
    Loads a JSON file and returns the corresponding Python object.
    
    Args:
        filename: The name of the input JSON file.
    
    Returns:
        The Python object parsed from the JSON file.
    """
    try:
        with open(filename) as f:
            try:
                x = json.load(f)
            except Exception as e:
                print(f"[{type(e).__name__}] {e}")
                sys.exit(1)

            return json.load(f)
    except Exception as e:
        print(f"[{type(e).__name__}] {e}")
