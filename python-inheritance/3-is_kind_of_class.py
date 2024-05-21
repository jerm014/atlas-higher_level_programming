#!/usr/bin/python3
"""Check if object is instance of class"""


def is_kind_of_class(obj, some_class):
    """Return True if object is instance of a class or a child class"""
    return (isinstance(obj, some_class))
