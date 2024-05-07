#!/usr/bin/python3
if __name__ != '__main__':
    exit


def list_division(a, b, c):
    errors = {"ZeroDivisionError": "division by 0",
              "TypeError": "wrong type",
              "IndexError": "out of range"}
    res = []
    for i in range(c):
        try:
            div = a[i] / b[i]
        except IndexError:
            print(errors["IndexError"])
        except TypeError:
            print(errors["TypeError"])
        except ZeroDivisionError:
            print(errors["ZeroDivisionError"])
        finally:
            res.append(div)
    return res
