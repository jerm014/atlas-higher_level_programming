#!/usr/bin/python3
'''This module has add_integer that adds 2 integers.'''


def add_integer(a, b=98):
    '''This function adds 2 integers

    Args:
        a (int): The first integer
        b (int): The second integer

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        int sum of a and b
    '''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
