#!/usr/bin/python3
"""unittests for base.py"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """test the class Base"""

    def test_id(self):
        """can we make a new Base"""
        Base._Base__nb_objects = 0
        base = Base()
        self.assertEqual(base.id, 1)

    def test_make_a_base(self):
        """do the id's make sense"""
        baseA = Base()
        baseB = Base()
        self.assertEquals(baseA.id, baseB.id - 1)

    def test_assign_id(self):
        """can we assign an id ourselves"""
        self.assertEqual(98, Base(98).id)

    def test_makes_a_base(self):
        """another test of making a new Base with default id"""
        self.assertIsNotNone(Base())

    def test_to_json_string(self):
        self.assertEquals(Base.to_json_string(None),"[]")

    def test_from_json_string(self):
        self.assertEquals(Base.from_json_string(None), [])

class Test_Base__save_to_file(unittest.TestCase):
    """test the base class save_to_file method"""

    @classmethod
    def tearDown(self):
        """delete files"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_1(self):
        r = Rectangle(11, 8, 1, 9, 3)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_2(self):
        r1 = Rectangle(11, 9, 1, 1, 1)
        r2 = Rectangle(1, 1, 1, 1, 1)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_3(self):
        s = Square(10, 1, 1, 1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_4(self):
        s1 = Square(10, 1, 1, 1)
        s2 = Square(2, 1, 1, 1)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_5(self):
        s = Square(10, 1, 1, 1)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_6(self):
        s = Square(3, 1, 10, 1)
        Square.save_to_file([s])
        s = Square(10, 1, 1, 1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_7(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_8(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_9(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_10(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)



class Test_Base__load_from_file(unittest.TestCase):
    """test the base class load_from_file method"""

    @classmethod
    def tearDown(self):
        """delete files"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_1(self):
        r1 = Rectangle(10, 1, 1, 1, 1)
        r2 = Rectangle(1, 1, 1, 1, 1)
        Rectangle.save_to_file([r1, r2])
        out = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(out[0]))

    def test_load_from_file_2(self):
        r1 = Rectangle(10, 1, 1, 1, 1)
        r2 = Rectangle(1, 1, 1, 1, 1)
        Rectangle.save_to_file([r1, r2])
        out = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(out[1]))

    def test_load_from_file_3(self):
        r1 = Rectangle(10, 1, 1, 1, 1)
        r2 = Rectangle(1, 1, 1, 1, 1)
        Rectangle.save_to_file([r1, r2])
        out = Rectangle.load_from_file()
        self.assertTrue(all(type(o) == Rectangle for o in out))

    def test_load_from_file_4(self):
        s1 = Square(1, 1, 1, 1)
        s2 = Square(1, 1, 1, 1)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_5(self):
        s1 = Square(1, 1, 1, 1)
        s2 = Square(1, 1, 1, 1)
        Square.save_to_file([s1, s2])
        list_squares_out = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_out[1]))

    def test_load_from_file_6(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        out = Square.load_from_file()
        self.assertTrue(all(type(o) == Square for o in out))

    def test_load_from_file_7(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_8(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

