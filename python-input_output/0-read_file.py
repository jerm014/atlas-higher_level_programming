#!/usr/bin/python3
"""documentation is important!"""


def read_file(filename=""):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
