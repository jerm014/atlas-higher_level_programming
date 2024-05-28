#!/usr/bin/python3
"""unittests for rectangle.py"""

import os
import unittest
from unittest.mock import patch
from io import StringIO
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

    def test_width_not_0(self):
        """can't assign a zero to the width!"""
        with self.assertRaises(ValueError):
            new = Rectangle(0, 1)

    def test_height_not_0(self):
        """can't assign a zero to the height!"""
        with self.assertRaises(ValueError):
            new = Rectangle(1, 0)

    def test_area(self):
        r = Rectangle(10, 10)
        self.assertEqual(r.area(), 100)

    def test_str(self):
        Base._Base__nb_objects = 0
        r = Rectangle(10, 10)
        self.assertEqual(str(r),"[Rectangle] (1) 0/0 - 10/10")

    def test_display_no_x_no_y(self):
        r = Rectangle(10, 2)
        out = "##########\n##########\n"
        with patch('sys.stdout', new=StringIO()) as stdout:
            r.display()
            self.assertEqual(stdout.getvalue(), out)

    def test_display_no_x(self):
        r = Rectangle(10, 2)
        r.y = 2
        out = "\n\n##########\n##########\n"
        with patch('sys.stdout', new=StringIO()) as stdout:
            r.display()
            self.assertEqual(stdout.getvalue(), out)

    def test_display_no_y(self):
        r = Rectangle(10, 2)
        r.x = 2
        out = "  ##########\n  ##########\n"
        with patch('sys.stdout', new=StringIO()) as stdout:
            r.display()
            self.assertEqual(stdout.getvalue(), out)

    def test_to_dictionary(self):
        Base._Base__nb_objects = 0
        r = Rectangle(10, 2)
        d = {'id': 1, 'width': 10, 'height': 2, 'x': 0, 'y': 0} 
        self.assertEqual(r.to_dictionary(), d)

    def test_update_1(self):
        r = Rectangle(10, 100, 1000, 10000, 1)
        r.update()
        self.assertEqual("[Rectangle] (1) 1000/10000 - 10/100", str(r))

    def test_update_2(self):
        r = Rectangle(10, 100, 1000, 10000, 1)
        r.update(2)
        self.assertEqual("[Rectangle] (2) 1000/10000 - 10/100", str(r))

    def test_update_3(self):
        r = Rectangle(10, 100, 1000, 10000, 1)
        r.update(2, 20)
        self.assertEqual("[Rectangle] (2) 1000/10000 - 20/100", str(r))

    def test_update_4(self):
        r = Rectangle(10, 100, 1000, 10000, 1)
        r.update(2, 20, 200)
        self.assertEqual("[Rectangle] (2) 1000/10000 - 20/200", str(r))

    def test_update_5(self):
        r = Rectangle(10, 100, 1000, 10000, 1)
        r.update(2, 20, 200, 2000)
        self.assertEqual("[Rectangle] (2) 2000/10000 - 20/200", str(r))

    def test_update_6(self):
        r = Rectangle(10, 100, 1000, 10000, 1)
        r.update(2, 20, 200, 2000, 20000)
        self.assertEqual("[Rectangle] (2) 2000/20000 - 20/200", str(r))

    def test_create_1(self):
        r = Rectangle.create(**{ 'id': 89 })
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")

    def test_create_2(self):
        r = Rectangle.create(**{ 'id': 89,
                                 'width': 2 })
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/1")

    def test_create_3(self):
        r = Rectangle.create(**{ 'id': 89,
                                 'width': 2,
                                 'height': 2 })
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/2")

    def test_create_4(self):
        r = Rectangle.create(**{ 'id': 89,
                                 'width': 2,
                                 'height': 2,
                                 'x': 2 })
        self.assertEqual(str(r), "[Rectangle] (89) 2/0 - 2/2")

    def test_create_5(self):
        r = Rectangle.create(**{ 'id': 89,
                                 'width': 2,
                                 'height': 2,
                                 'x': 2,
                                 'y': 2 })
        self.assertEqual(str(r), "[Rectangle] (89) 2/2 - 2/2")

    def test_save_to_file_none(self):
        r = Rectangle(1,1)
        self.assertEqual(r.save_to_file(None), None)

    def test_save_to_file_emptylist(self):
        r = Rectangle(1,1)
        self.assertEqual(r.save_to_file([]), None)


#Rectangle.create(**{ 'id': 89, 'width': 1 })
#Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })
#Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
#Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
#Rectangle.save_to_file(None)
#Rectangle.save_to_file([])
#Rectangle.save_to_file([Rectangle(1, 2)])
#Rectangle.load_from_file() # file doesn't exist
#Rectangle.load_from_file() # file does exist


