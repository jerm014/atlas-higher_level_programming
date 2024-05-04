#!/usr/bin/python3
if __name__ != '__main__':
    exit


def element_at(a, b):
    last_element = len(a) - 1
    if b < 0 or b > last_element:
        return "None"
    else:
        return a(b)
