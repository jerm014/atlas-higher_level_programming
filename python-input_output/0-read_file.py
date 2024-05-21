#!/usr/bin/python3
"""documentation is important!"""


def read_file(filename=""):
    """documentation for the function!"""
    ERR_NOFILE = "[FileNotFoundError] [Errno 2] No such file or directory: '{}'"
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print(ERR_NOFILE, filename)
    except Exception as e:
        print(f"An error occurred: {e}")
