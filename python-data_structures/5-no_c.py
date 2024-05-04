#!/usr/bin/python3
if __name__ != '__main__':
    exit


def no_c(a):
    res = ""
    for i in range(0, len(a)):
        if a[i] != "c" and a[i] != "C":
            res += a[i]
    return res

