#!/usr/bin/python3
if __name__ != '__main__':
    exit


def safe_print_list_integers(a=[], b=0):
    printed = 0
    for i in range(0, b):
        try:
            print("{:d}".format(a[i]), end="")
            printed += 1
        except (TypeError, ValueError):
            continue
    print()
    return printed
