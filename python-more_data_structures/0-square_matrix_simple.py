#!/usr/bin/python3
if __name__ != '__main__':
    exit


def square_matrix_simple(a=[]):
    return list(map(square_matrix, a))


def square_matrix(a):
    return list(map(pow2, a))


def pow2(a):
    return a ** 2
