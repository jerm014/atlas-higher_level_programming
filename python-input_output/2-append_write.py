#!/usr/bin/python3
"""documentation is important!"""


def append_write(filename="", text=""):
    """ function documentation goes here!"""
    try:
        with open(filename, "a", encoding="utf-8") as file:
            num_chars_added = file.write(text)
            return num_chars_added
    except FileNotFoundError:
        # Create the file if it doesn't exist
        with open(filename, "w", encoding="utf-8") as new_file:
            num_chars_added = new_file.write(text)
            return num_chars_added
