#!/usr/bin/python3
if __name__ != '__main__':
    exit


def delete_at(a=[], b=0):
    last_element = len(a) - 1
    if b < 0 or b > last_element:
        return a

    del a[b]
    return a
