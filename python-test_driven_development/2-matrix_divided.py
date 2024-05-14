#!/usr/bin/python3
'''This module divides all elements of matrix'''


def matrix_divided(matrix, div):
    '''Divide elements of matrix
    Args:
        matrix (list):    a matrix (list of lists)
        div (int, float): the divisor

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    Returns:
        list: A matrix result of the divided matrix
    '''
    err_msg = "matrix must be a matrix(list of lists) of integers/floats"
    err_size = "Each row of the matrix must have the same size"
    err_number = "div must be a number"
    err_divzero = "division by zero"

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(el, int) or isinstance(el, float))
                    for el in [num for row in matrix for num in row])):
        raise TypeError(err_msg)

    for row in matrix:
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(err_msg)

    row_length = set(len(row) for row in matrix)
    if len(row_length) != 1:
        raise TypeError(err_size)

    if not isinstance(div, (int, float)):
        raise TypeError(err_number)
    if div == 0:
        raise ZeroDivisionError(err_divzero)

    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            new_elem = round(elem / div, 2)
            new_row.append(new_elem)
        new_matrix.append(new_row)

    return new_matrix
