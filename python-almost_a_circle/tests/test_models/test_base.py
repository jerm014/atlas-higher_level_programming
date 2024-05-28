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
