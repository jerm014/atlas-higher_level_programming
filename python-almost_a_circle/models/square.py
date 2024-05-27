#!/usr/bin/python3
"""File for class Rectangle, which inherits from class Base"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square, inherited from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """init a square"""
        super().__init__(size, size, x, y, id)
