#!/usr/bin/python3
import random
number = random.randint(-10, 10)
res = ["is zero", "is positive", "is negative"]
if number == 0:
    print(f"{number} {res[0]}")
elif number > 0:
    print(f"{number} {res[1]}")
else:
    print(f"{number} {res[2]}")
