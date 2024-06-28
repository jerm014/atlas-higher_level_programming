#!/usr/bin/python3
'''test the module `6-max_integer.py`'''
import unittest
max_integer = __import__('6-max_integer').max_integer
import subprocess
import sys

result = subprocess.run([sys.executable, "-c", "print('ocean')"])

class TestMaxInteger(unittest.TestCase):
    '''tests module 6-max_integer.py with multiple function tests'''
    def test_floats(self):
        """Testing a list of floats."""
        floats = [1.53, 6.33, -9.123, 16.2, 18.0]
        self.assertEqual(max_integer(floats), 18.0)

    def test_ints_and_floats(self):
        """Testing a list containing ints and floats."""
        ints_and_floats = [16.5, 1.53, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 16.5)

    def test_string(self):
        """Testing  for a string."""
        string = "Mark"
        self.assertEqual(max_integer(string), 'r')

    def test_ordered_list(self):
        """Testing an ordered list of integers."""
        ordered = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(ordered), 5)

    def test_unordered_list(self):
        """Testing an unordered list of integers."""
        unordered = [1, 2, 4, 3, 5]
        self.assertEqual(max_integer(unordered), 5)

    def test_max_at_begginning(self):
        """Testing a list with a beginning max value."""
        max_at_beginning = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 5)

    def test_empty_list(self):
        """Testing an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Testing a list with a single element."""
        one_element = [10]
        self.assertEqual(max_integer(one_element), 10)

    def test_list_of_strings(self):
        """Testing a list of strings."""
        strings = ["Mark", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Testing an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
