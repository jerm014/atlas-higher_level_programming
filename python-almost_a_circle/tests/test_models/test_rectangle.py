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
        """test it another way"""
        self.assertIsNotNone(Rectangle(1, 2))

    def test_new_rectangle3(self):
        """make a new rectangle and give it attributes"""
        Base._Base__nb_objects = 0  # reset the count
        new = Rectangle(1, 2)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_width_not_a_string1(self):
        """can't assign a string to the width!"""
        with self.assertRaises(TypeError):
            new = Rectangle("1", 1)

    def test_height_not_a_string2(self):
        """can't assign a string to the height!"""
        with self.assertRaises(TypeError):
            new = Rectangle(1, "1")

    def test_x_not_a_string3(self):
        """can't assign a string to the x!"""
        with self.assertRaises(TypeError):
            new = Rectangle(1, 1, "1")

    def test_y_not_a_string4(self):
        """can't assign a string to the y!"""
        with self.assertRaises(TypeError):
            new = Rectangle(1, 1, 1, "1")

    def test_make_rectangle_with_all_5(self):
        new = Rectangle(1, 10, 100, 1000, 10000)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 10)
        self.assertEqual(new.x, 100)
        self.assertEqual(new.y, 1000)
        self.assertEqual(new.id, 10000)

    def test_width_not_below_0(self):
        """can't assign a negative to the width!"""
        with self.assertRaises(ValueError):
            new = Rectangle(-1, 1)

    def test_height_not_below_0(self):
        """can't assign a negative to the height!"""
        with self.assertRaises(ValueError):
            new = Rectangle(1, -1)

    def test_x_not_below_0(self):
        """can't assign a negative to the x!"""
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, -1)

    def test_y_not_below_0(self):
        """can't assign a negative to the y!"""
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, 1, -1)
