#!/usr/bin/python3
"""LATE"""


def pascal_triangle(i):
    """Dumb Triangle"""
    if i <= 0:
        return []

    pt = [[1]]
    while len(pt) != i:
        triangle = pt[-1]
        temp = [1]
        for x in range(len(triangle) - 1):
            temp.append(triangle[x] + triangle[x + 1])
        temp.append(1)
        pt.append(temp)
    return pt
