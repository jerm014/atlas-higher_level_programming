#!/usr/bin/python3
def uppercase(a):
    res = ""
    for i in a:
        if (ord(i) >= ord("a") and ord(i) <= ord("z")):
            res += chr(ord(i) - 32)
        else:
            res += i
    print(res.format())
