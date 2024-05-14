#!/usr/bin/python3
'''This module contains a square class and some methods for manipulating
'''


class Square:
    '''This is a square class

    Attributes:
        size (int): size of the square
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''This function initializes the square object

        Args:
            size (int): size of the square
            position (tuple): 2 positive integers for the position of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
            TypeError: if position is not a tuple of 2 positive integers
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        if isinstance(position, tuple) and len(position) == 2:
            if all(isinstance(item, int) and item >= 0 for item in position):
                self.__position = position
            else:
                raise TypeError(
                        "position must be a tuple of 2 positive integers"
                    )
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        '''This function is to get or set the size

        Returns:
            (int): size of the square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''This function is for setting the size of the square

        Args:
        value (int): This is the value to set the size of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than zero.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        '''This funcion gets or sets the position of the square

        Returns:
            (tuple): position of the square
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''This function sets the position of the square to a new psition

        Args:
            value (tuple): 2 positive integers

        Raises:
            TypeError: If value does not contain 2 positive integers
        '''
        if isinstance(value, tuple) and len(value) == 2:
            if all(isinstance(item, int) and item >= 0 for item in value):
                self.__position = value
            else:
                raise TypeError(
                        "position must be a tuple of 2 positive integers"
                    )
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        '''This function gets the area of a square

        Returns:
            int: area of the square
        '''
        return self.__size * self.__size

    def my_print(self):
        '''This function prints out a square in stdout using #

        if size is 0, it prints an empty line

        Returns:
            None
        '''
        if self.__size == 0:
            print()

        [print() for i in range(self.position[1])]
        for j in range(self.__size):
            [print(" ", end="") for i in range(self.position[0])]
            for i in range(self.__size):
                print("#", end="")

            print()

    def __str__(self):
        '''Stringify a square object'''
        if self.__size != 0:
            [print() for j in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for i in range(self.__position[0])]
            [print("#", end="") for m in range(self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
