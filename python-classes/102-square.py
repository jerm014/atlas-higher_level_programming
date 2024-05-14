#!/usr/bin/python3
'''This module contains a square class and some methods for manipulating
'''


class Square:
    '''This is a square class

    Attributes:
        size (int): size of the square
    '''
    def __init__(self, size=0):
        '''This function initializes square

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

    @property
    def size(self):
        '''This function is used to get or set the size of the square

        Returns:
            (int): size of the square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''This function is used for setting the size

        Args:
            value (int): size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        '''This function gets the area

        Returns:
            int: area of the square
        '''
        return self.__size * self.__size

    def __gt__(self, other):
        '''Checks if this is greater than

        Returns:
            (bool): True or False.
        '''
        return self.area() > other.area()

    def __eq__(self, other):
        '''Checks for equality

        Returns:
            (bool): True or False.
        '''
        return self.area() == other.area()

    def __ne__(self, other):
        '''Checks for non equality

        Returns:
            (bool): True or False.
        '''
        return self.area() != other.area()

    def __ge__(self, other):
        '''Checks for greater than or equal

        Returns:
            (bool): True or False.
        '''
        return self.area() >= other.area()

    def __lt__(self, other):
        '''Checks for less than

        Returns:
            (bool): True or False.
        '''
        return self.area() < other.area()

    def __le__(self, other):
        '''Checks for the less than or equal

        Returns:
            (bool): True or False.
        '''
        return self.area() <= other.area()
