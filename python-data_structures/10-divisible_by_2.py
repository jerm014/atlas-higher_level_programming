#!/usr/bin/python3
if __name__ != '__main__':
    exit

def divisible_by_2(a=[]):
    res = []
    for i in a:
        res.append(i % 2 == 0)
    return res
