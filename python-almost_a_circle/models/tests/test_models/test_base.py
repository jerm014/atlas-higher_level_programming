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
    def test_make_a_base(self):
        baseA = Base()
        baseB = Base()
        self.assertEquals(baseA.id, baseB.id - 1)

    def test_assign_id(self):
        self.assertEqual(98, Base(98).id)

