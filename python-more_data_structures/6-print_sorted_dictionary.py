#!/usr/bin/python3
if __name__ != '__main__':
    exit


def print_sorted_dictionary(a):
    sorted_dict_by_keys = dict(sorted(a.items()))
    for i in sorted_dict_by_keys:
        print("{}: {}".format(i, sorted_dict_by_keys[i]))
