#!/usr/bin/python3
"""documentation is important!"""
import json

def load_from_json_file(filename):
    """
    Loads a JSON file and returns the corresponding Python object.
    
    Args:
        filename: The name of the input JSON file.
    
    Returns:
        The Python object parsed from the JSON file.
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"[JSONDecodeError] {e}")
        return None
    except PermissionError:
        pass
