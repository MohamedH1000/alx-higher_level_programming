#!/usr/bin/python3
"""a unittest for max integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    a problem that test max integer
    """

    def test_the_max(self):
        self.assertEqual(max_integer([4, 7, 2]), 7)
        self.assertEqual(max_integer([7, 4, 2]), 7)
        self.assertEqual(max_integer([5, 6, 2]), 6)
        self.assertEqual(max_integer([6, 6, 1]), 6)
        self.assertEqual(max_integer([12, 4, 13]), 13)
        self.assertEqual(max_integer([-10, -6, 0]), 0)
        self.assertEqual(max_integer([-7, -99, -1]), -1)
        self.assertEqual(max_integer([0, -0, 0]), 0)
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-2]), -2)
        self.assertEqual(max_integer([0.4]), 0.4)
        self.assertEqual(max_integer([0.3, 0.5, -0.1]), 0.5)
        self.assertEqual(max_integer([-4.3, -4.4, -4.9]), -4.3)

    def test_the_max_emp(self):
        self.assertEqual(max_integer([]), None)

    def test_the_max_neg(self):
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer("promax"), max("promax"))
        self.assertEqual(max_integer([0, -0, -0.9]), 0)
        self.assertEqual(max_integer([-100000.1, -97.9, -1000.1]), -97.9)
        self.assertEqual(max_integer([112.5, 96.5, 30.0]), 112.5)
        self.assertEqual(max_integer([0.0000000000000000000007,
        0.0000000000000000000000000007]), 0.0000000000000000000007)
        self.assertEqual(max_integer([1.0000005, 1.0000009]), 1.0000009)
        self.assertEqual(max_integer("01234567890sS"), max("01234567890sS"))
        self.assertEqual(max_integer([[1, 2, 3], [-100]]), \
            max([[1, 2, 3], [-100]]))
        self.assertEqual(max_integer([float('-inf'), float('inf')]),\
            max([float('-inf'), float('inf')]))

    def test_errors(self):
        with self.assertRaises(TypeError):
            max_integer(False)
        with self.assertRaises(TypeError):
            max_integer(-5555555)
        with self.assertRaises(TypeError):
            max_integer(5555555)
