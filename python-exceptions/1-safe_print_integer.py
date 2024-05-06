#!/usr/bin/python3
if __name__ != '__main__':
    exit


def safe_print_integer(value):
    try:
        print()"{:d}".format(value))
        return True
    except Exception as e:
        return False
