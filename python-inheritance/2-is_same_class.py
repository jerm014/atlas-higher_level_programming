#!/usr/bin/python3
"""Checks if object is instance of class"""


def is_same_class(obj, some_class):
    """Returns True if object is instance of class"""
    return (some_class is type(obj))
