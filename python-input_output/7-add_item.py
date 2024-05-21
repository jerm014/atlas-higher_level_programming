#!/usr/bin/python3
#load add save
"""documentation is important!"""
import sys
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj (object): The Python object to be serialized.
        filename (str):  The name of the file to write.

    Notes:
        - Uses the 'with' statement for proper file handling.
        - Does not handle exceptions if the object cannot be serialized.
        - Does not manage file permission exceptions.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)


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
    except FileNotFoundError as e:
        print(f"[FileNotFoundError] {e}")


try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []
items.extend(sys.argv[1:])
save_to_json_file(items, "add_item.json")
