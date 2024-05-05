#!/usr/bin/python3
if __name__ != '__main__':
    exit


def uniq_add(my_list=[]):
    res = 0
    res_arr = list(set(my_list))
    for i in res_arr:
        res += i
    return res
