#!/usr/bin/python3
if __name__ != '__main__':
    exit


def safe_print_list(a=[], x=0):
    res = 0
    try:
        for i in a:
            print(i, end="")
            res += 1
            if res == x:
                break
    except:
        return res
    finally:
        print()
        return res
