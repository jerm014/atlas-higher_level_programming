#!/usr/bin/python3
if __name__ != '__main__':
    exit

import hidden_4
a = dir(hidden_4)
for i in a:
    if i[:2] != "__":
        print(i)
