#!/usr/bin/python3
"""Fiile for class Base"""
import json
import os


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
                j = self.to_json_string([i.to_dictionary() for i in list_objs])
                text_file.write(j)

    @staticmethod
    def from_json_string(json_string):
        """return the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create a new thing from dictionary information"""
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        else:
            obj = cls(1)

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instnaces:"""

        file_name = cls.__name__ + ".json"
        instance = []
        dictionary = []

        if os.path.exists(file_name):
            with open(file_name, 'r') as text_file:
                json_str = text_file.read()
                dictionary = cls.from_json_string(json_str)
                for d in dictionary:
                    instance.append(cls.create(**d))
        return instance
