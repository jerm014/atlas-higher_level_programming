#!/usr/bin/python3
if __name__ != '__main__':
    exit


def safe_print_list_integers(a=[], b=0):
    printed = 0
    try:
        for i in range(0, b + 1):
            print(a[i], end="")
            printed += 1
            if printed == b:
                return printed
    except (TypeError, ValueError):
        pass
    except (IndexError) as e:
        raise IndexError(e)
    finally:
        print()

    return printed
