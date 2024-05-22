#!/usr/bin/python3
"""documentation is important!"""
import json


def load_from_json_file(filename):
    """Loads a JSON file and returns the corresponding Python object."""
    with open(filename) as f:
        return json.load(f)
