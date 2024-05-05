#!/usr/bin/python3
if __name__ != '__main__':
    exit


def best_score(a):
    key = "None"
    value = "None"
    try:
        for i in a:
            if key == "None" or a[i] > value:
                key = i
                value = a[i]
    except NoneType as e:
        key = "None"
    finally:
        return key
