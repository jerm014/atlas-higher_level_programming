#!/usr/bin/python3
if __name__ != '__main__':
    exit


def max_integer(a=[]):
    if len(a) == 0:
        return "None"
    res = a[0]
    for i in a:
        if i > res:
            res = i
    return res
