#!/usr/bin/python3
"""Defines unittests for base.py.
Unittest classes:

"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Rectangle(unittest.TestCase):
    """test instantiation of the class Base"""

    def test_new_rectangle(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2)
        self.assertEqual(r1.id, r2.id - 1)
