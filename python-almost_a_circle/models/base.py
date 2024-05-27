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

    @classmethod
    def save_to_file(self, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        file_name = self.__name__ + ".json"
        with open(file_name, "w") as text_file:
            if list_objs is None:
                text_file.write("[]")
            else:
                j = Base.to_json_string([i.to_dictionary() for i in list_objs])
                text_file.write(j)
