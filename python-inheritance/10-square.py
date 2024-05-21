#!/usr/bin/python3
"""documentation"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """make a square"""

    def __init__(self, size):
        """make new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
