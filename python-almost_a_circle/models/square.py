#!/usr/bin/python3
"""File for class Rectangle, which inherits from class Base"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square, inherited from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """init a square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """just call the rectangle update"""
        super().update(args, kwargs)
