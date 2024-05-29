#!/usr/bin/python3
"""Defines unittests for base.py.
Unittest classes:

"""
import os
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Square(unittest.TestCase):
    """test Square class"""

    def test_square_1(self):
        self.assertIsInstance(Square(10), Base)

    def test_square_2(self):
        self.assertIsInstance(Square(10), Square)

    def test_square_3(self):
        with self.assertRaises(TypeError):
            Square()

    def test_square_4(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_square_5(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_square_6(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_square_7(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_square_8(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_square_9(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_square_10(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_square_11(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_square_12(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_square_13(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_square_14(self):
        self.assertEqual(0, Square(10).x)

    def test_square_15(self):
        self.assertEqual(0, Square(10).y)

    def test_square_16(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_square_17(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_square_18(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)

    def test_square_19(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_square_20(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -1, 0)

    def test_square_21(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, None)

    def test_square_22(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 0, -1)

    def test_square_23(self):
        self.assertEqual(100, Square(10).area())

    @staticmethod
    def capture_stdout(sq, method):
        """Captures text from stdout

        Args:
            sq (Square): The Square to display
            method (str): The method to run on sq.
        Returns:
            The text to stdout from method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_square_24(self):
        s = Square(4)
        cap = Test_Square.capture_stdout(s, "print")
        res = "[Square] ({}) 0/0 - 4\n".format(s.id)
        self.assertEqual(res, cap.getvalue())

    def test_square_25(self):
        s = Square(5, 5)
        res = "[Square] ({}) 5/0 - 5".format(s.id)
        self.assertEqual(res, str(s))

    def test_square_26(self):
        s = Square(7, 4, 22)
        res = "[Square] ({}) 4/22 - 7".format(s.id)
        self.assertEqual(res, str(s))

    def test_square_27(self):
        s = Square(5, 10, 20, 100)
        self.assertEqual("[Square] (100) 10/20 - 5", str(s))

    def test_square_28(self):
        s = Square(2)
        cap = Test_Square.capture_stdout(s, "display")
        self.assertEqual("##\n##\n", cap.getvalue())

    def test_square_29(self):
        s = Square(3, 1, 0)
        cap = Test_Square.capture_stdout(s, "display")
        self.assertEqual(" ###\n ###\n ###\n", cap.getvalue())

    def test_square_30(self):
        s = Square(4, 0, 1)
        cap = Test_Square.capture_stdout(s, "display")
        res = "\n####\n####\n####\n####\n"
        self.assertEqual(res, cap.getvalue())

    def test_square_31(self):
        s = Square(2, 3, 2)
        cap = Test_Square.capture_stdout(s, "display")
        res = "\n\n   ##\n   ##\n"
        self.assertEqual(res, cap.getvalue())

    def test_square_32(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.display(1)

    def test_square_33(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_square_34(self):
        s = Square(10, 10, 10, 10)
        s.update(1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(s))

    def test_square_35(self):
        s = Square(10, 10, 10, 10)
        s.update(1, 2)
        self.assertEqual("[Square] (1) 10/10 - 2", str(s))

    def test_square_36(self):
        s = Square(10, 10, 10, 10)
        s.update(1, 2, 3)
        self.assertEqual("[Square] (1) 3/10 - 2", str(s))

    def test_square_37(self):
        s = Square(10, 10, 10, 10)
        s.update(1, 2, 3, 4)
        self.assertEqual("[Square] (1) 3/4 - 2", str(s))

    def test_square_38(self):
        s = Square(10, 10, 10, 10)
        s.update(1, 2, 3, 4, 5)
        self.assertEqual("[Square] (1) 3/4 - 2", str(s))

    def test_square_39(self):
        s = Square(10, 10, 10, 10)
        s.update(None)
        res = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(res, str(s))

    def test_square_40(self):
        s = Square(10, 10, 10, 10)
        s.update(None, 4, 5)
        res = "[Square] ({}) 5/10 - 4".format(s.id)
        self.assertEqual(res, str(s))

    def test_square_41(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(1, "invalid")

    def test_square_42(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(1, 0)

    def test_square_43(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(1, -4)

    def test_square_44(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(1, 1, "invalid")

    def test_square_45(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(1, 1, -4)

    def test_square_46(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(1, 1, 2, "invalid")

    def test_square_47(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(1, 1, 2, -4)

    def test_square_48(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(1, "invalid", "invalid")

    def test_square_to_dictionary_1(self):
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_square_to_dictionary_2(self):
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_square_to_dictionary_3(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)
