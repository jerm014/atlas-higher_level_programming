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
    def to_json_string(list_of_dictionaries):
        """convert a list of dictionaries to a json string"""
        if list_of_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_of_dictionaries)

    def save_to_file(cls, list_objs=None):
        """writes the JSON string representation of list_objs to a file"""
        json_string = Base.to_json_string(list_objs)
        file_name = "Rectangle.json"
        with open(file_name, "w+") as text_file:
            text_file.write(json_string)
