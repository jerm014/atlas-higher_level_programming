#!/usr/bin/python3
'''This module prints a square'''


def print_square(size):
    '''Prints a square using "#"

    Args:
        size (int): size of the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    '''

    err_integer = "size must be an integer"
    err_eq_gt_zero = "size must be >= 0"

    if not isinstance(size, int):
        raise TypeError(err_integer)
    if size < 0:
        raise ValueError(err_eq_gt_zero)
    if size < 0 and isinstance(size, float):
        raise TypeError(err_integer)

    for width in range(0, size):
        for length in range(0, size):
            print("#", end="")
        print()
