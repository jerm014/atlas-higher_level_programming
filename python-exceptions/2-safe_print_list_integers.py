#!/usr/bin/python3
if __name__ != '__main__':
    exit


def safe_print_list_integers(a=[], b=0):
    printed = 1
    try:
        for i in range(0, b):
            if printed == b:
                return printed
            print("{:d}".format(a[i]), end="")
            printed += 1
        print()
    except (TypeError, ValueError):
        pass
    #except (IndexError) as e:
    #    print(e)

    return printed
