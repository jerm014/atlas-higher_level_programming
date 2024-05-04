#!/usr/bin/python3
if __name__ != '__main__':
    exit


def add_tuple(a=(), b=()):
    res1 = 0
    res2 = 0
    res3 = 0
    res4 = 0

    if len(a) >= 1:
        res1 = a[0]
    if len(a) >= 2:
        res2 = a[1]
    if len(b) >= 1:
        res3 = b[0]
    if len(b) >= 2:
        res4 = b[1]

    return tuple((res1 + res2, res3 + res4))
