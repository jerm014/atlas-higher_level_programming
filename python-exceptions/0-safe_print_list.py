#!/usr/bin/python3
if __name__ != '__main__':
    exit


def safe_print_list(a=[], x=0):
    res = 0
    try:
        for i in a:
            if res == x:
                break
            print(i, end="")
            res += 1
    except Exception as e:
        return res
    finally:
        print()
        return res
