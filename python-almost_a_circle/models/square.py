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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value
