#!/usr/bin/python3
"""Defines unittests for base.py.
Unittest classes:
    TestBase_instantiation - line 14

"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """test instantiation of the class Base"""
    def test_new_base(self):
        """can we make a new Base"""
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

