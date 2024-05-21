#!/usr/bin/python3
"""documentaion"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """moar documenattion"""

    def __init__(self, width, height):
        """make new rectangle"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns pretty Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
