#!/usr/bin/python3
"""Module that inherits from the list class"""


class MyList(list):
    """Class that inherits from list class"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
