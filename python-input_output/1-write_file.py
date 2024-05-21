#!/usr/bin/python3
"""documentation is important!"""


def write_file(filename="", text=""):
    """function documentation goes right here."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            num_chars_written = file.write(text)
            return num_chars_written
    except FileNotFoundError:
        # Create the file if it doesn't exist
        with open(filename, "w", encoding="utf-8") as new_file:
            num_chars_written = new_file.write(text)
            return num_chars_written
