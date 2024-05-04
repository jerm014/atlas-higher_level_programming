#!/usr/bin/python3
if __name__ != '__main__':
    exit


def print_reversed_list_integer(a=[]):
    i = len(a) - 1
    while i > 0:
        print("{}".format(a[i]))
        i -= 1
