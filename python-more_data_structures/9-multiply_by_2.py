#!/usr/bin/python3
if __name__ != '__main__':
    exit


def multiply_by_2(a):
    a = a.copy()
    for key, value in a.items():
        a[key] = value * 2
    return a
