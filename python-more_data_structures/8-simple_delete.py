#!/usr/bin/python3
if __name__ != '__main__':
    exit


def simple_delete(a, key=""):
    try:
        a.pop(key)
    finally:
        return a
