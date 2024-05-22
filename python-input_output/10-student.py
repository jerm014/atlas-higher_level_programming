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
        if attrs is None:
            return self.__dict__
        else:
            return [self.__dict__ in attrs]
