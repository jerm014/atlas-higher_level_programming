#!/usr/bin/python3
'''This module contains a square class and some methods for manipulating
'''


class Square:
    '''This is a square class

    Attributes:
        size (int): size of the square
    '''
    def __init__(self, size=0):
        '''This function initializes a square

        Args:
            size (int): size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
