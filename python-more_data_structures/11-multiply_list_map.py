#!/usr/bin/python3
if __name__ != '__main__':
    exit


def multiply_list_map(a=[], number=0):
    iter2 = [number] * len(a)
    return list(map(mul, a, iter2))


def mul(a, b):
    return a * b 
