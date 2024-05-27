#!/usr/bin/python3
"""Fiile for class Base"""
import json


class Base:
    """Base Class for Shapes"""

    id = 0
    __nb_objects = 0

    def __init__(self, id=None):
        """base init function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert a list of dictionaries to json"""
        return json.dumps(list_dictionaries)
