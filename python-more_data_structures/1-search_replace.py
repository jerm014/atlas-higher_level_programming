#!/usr/bin/python3
if __name__ != '__main__':
    exit


def search_replace(a, search, replace):
    res = []
    for i in a:
        if i == search:
            res.append(replace)
        else:
            res.append(i)

    return res
