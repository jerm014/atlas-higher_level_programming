#!/usr/bin/python3
if __name__ != '__main__':
    exit

    
def safe_print_division(a, b):
    res = None
    try:
        res = a / b
    except ZeroDivisionError:
        pass
    except Exception as e:
        print("Exception:{}".format(e))
    finally:
        print("Inside result: {}".format(res))
        return res
