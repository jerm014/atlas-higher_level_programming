#!/usr/bin/python3
'''TThis module does rectangle things'''


class Rectangle:
    '''Rectangle class

    Attributes:
        width (int): width of rectangle
        height (int): height of threctangle
    '''
    def __init__(self, width=0, height=0):
        '''Initializes a rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle

        Raises:
            TypeError: width or height is not an integer
            ValueError: width or height is less than 0
        '''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        '''Used ot get or access the attribute width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''This sets the width attribute of the object to a new value

        Args:
            value (int): The value to be checked before setting the attribute

        Raises:
            TypeError: When the value is not an integer
            ValueError: When the value is less than 0
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Gets or access the attribute height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''This sets the height attribute of the object to a new value

        Args:
            value (int): The value to be checked before setting the attribute

        Raises:
            TypeError: When the value is not an integer
            ValueError: When the value is less than 0'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
