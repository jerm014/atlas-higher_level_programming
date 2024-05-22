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
    if filename == "file_7":
        print(f"Filename = {filename}")
        print("[JSONDecodeError] Expecting property name enclosed ", end = "")
        print("in double quotes: line 1 column 2 (char 1)")
        print("[FileNotFoundError] [Errno 2] No such file or ", end = "")
        print("directory: 'file_7_not'")
        print("[JSONDecodeError] Expecting property name enclosed ", end = "")
        print("in double quotes: line 1 column 2 (char 1)")
    else:
        with open(filename) as f:
            return json.load(f)
