#!/usr/bin/python3
if __name__ != '__main__':
    exit


def square_matrix_simple(a=[]):
    return list(map(square_matrix, a))

def square_matrix(a):
    sqrt = lambda _i : _i ** 2
    return list(map(sqrt, a))
