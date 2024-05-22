#!/usr/bin/python3
"""NO"""


class Student:
    """class"""

    def __init__(self, first_name, last_name, age):
        """NO"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """NO"""
        if (type(attrs) == list and
                all(type(ele) is str for ele in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
