#!/usr/bin/python3
for i in range(0, 100):
    print("{:02d}".format(i), end="")
    if i < 99:
        comma = ", "
        cr = ""
    else:
        comma = ""
        cr = chr(10)
    print(comma.format(), end=cr)
