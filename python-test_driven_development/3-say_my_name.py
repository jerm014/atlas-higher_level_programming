#!/usr/bin/python3
'''This module prints first name and last name'''


def say_my_name(first_name, last_name=""):
    '''Prints "My name is <first name> <last name>"
    Args:
        first_name (string): first name
        last_name (string): last name

    Raises:
        TypeError: first_name must be a string
        TypeErro: last_name must be a string
    '''

    err_first = "first_name must be a string"
    err_last = "last_name must be a string"

    if not isinstance(first_name, str):
        raise TypeError(err_first)
    elif not isinstance(last_name, str):
        raise TypeError(err_last)
    else:
        print("My name is {} {}".format(first_name, last_name))
