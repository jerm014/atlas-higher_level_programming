#!/usr/bin/python3
"""documentation is important!"""
import json
import sys


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
    try:
        with open(filename, 'w') as f:
            try:
                x = json.dumps(my_obj)
            except Exception as e:
                print(f"[{type(e).__name__}] {e}")
                sys.exit(1)

            f.write(x)

    except Exception as e:
        print(f"[{type(e).__name__}] {e}")
