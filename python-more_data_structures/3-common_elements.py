#!/usr/bin/python3
if __name__ != '__main__':
    exit


def common_elements(set_1, set_2):
    res = []
    x = -1
    for i in set_1:
        try:
            x = list(set_2).index(i)
        except ValueError as e:
            x = -1
        finally:
            if x >= 0:
                res.append(i)
    return res
