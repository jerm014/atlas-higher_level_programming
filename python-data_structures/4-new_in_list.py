#!/usr/bin/python3
if __name__ != '__main__':
    exit


def new_in_list(a, b, c):
    last_element = len(a) - 1
    if b < 0 or b > last_element:
        return a
    a = a.copy()
    a[b] = c
    return a
