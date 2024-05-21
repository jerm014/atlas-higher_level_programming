#!/usr/bin/python3
"""Check if object is instance inherited from the specified class"""


def inherits_from(obj, some_class):
    """Return True if object is an instance of a class that inherited from the
    specified class
    """
    return (issubclass(type(obj), some_class) and (some_class is not type(obj)))
