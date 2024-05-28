#!/usr/bin/python3
"""unittests for rectangle.py"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Rectangle(unittest.TestCase):
    """test instantiation of the class Rectangle"""

    def test_new_rectangle(self):
        """can we make rectangles"""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_new_rectangle2(self):
        self.assertIsNotNone(Rectangle(1, 2))
