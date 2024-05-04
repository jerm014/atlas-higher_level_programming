#!/usr/bin/python3
if __name__ != '__main__':
    exit


def multiple_returns(a):
    length = len(a)
    if length > 0:
        first_character = a[:1]
    else:
        first_character = "None"

    return tuple((length, first_character))
