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
        """update the square"""
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

        if kwargs is not None and args is not None:
            for key, value in kwargs.items():
                if key == "size":
                    self.width = value
                    self.height = value
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """return a dictionary describing the shape"""
        d = {"id": self.id,
             "size": self.width,
             "x": self.x,
             "y": self.y}
        return d
