#!/usr/bin/python3
if __name__ != '__main__':
    exit


def add_tuple(a=(), b=()):
    c = (0, 0)

    if len(a) == 0:
        a = [0, 0]
    elif len(a) == 1:
        a[1] = 0

    if len(b) == 0:
        b = [0, 0]
    elif len(b) == 1:
        b[1] = 0

    return tuple(a[0] + b[0], a[1] + b[1])
