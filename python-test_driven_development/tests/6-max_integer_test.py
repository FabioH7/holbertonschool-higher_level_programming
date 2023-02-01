#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 2, 5, 4]), 5)
        self.assertAlmostEqual(max_integer([6, 2, 5, 4]), 6)
        self.assertAlmostEqual(max_integer([1, 2, -3, -1]), 2)
        self.assertAlmostEqual(max_integer([-5, -7, -2, -4]), -2)
        self.assertAlmostEqual(max_integer([4]), 4)
        self.assertAlmostEqual(max_integer(), None)
