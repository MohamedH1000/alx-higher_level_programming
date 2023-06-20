#!/usr/bin/python3
"""square unit tests for this module"""
import unittest
import io
from random import randrange
from contextlib import redirect_stdout
from models.base import Base
from models.square import Square


class testSquare(unittest.TestCase):
    """a class that test the square"""

    def setUp(self):
        """instatias class, import module"""
        Base._Base__nb_of_objects = 0

    def tearDown(self):
        """after each test method to clean up"""
        pass

    def test_a_class(self):
        """a square class type to be tested"""
        self.assertEqual(str(Square),"<class 'models.square.Square'>")

    def test_b_inheritance(self):
        """inhertance base of square to be tested"""
        self.assertTrue(issubclass(Square, Base))

    def test_c_no_args_constructor(self):
        """signature of the contruction to be tested"""
        with self.assertRaises(TypeError) as exc:
            rec = Square(4, 5, 6, 7, 8)
        s = "__init__() takes from 2 to 5 positional arguments but 6 \
            were given"

    def test_d_instantiation_keyword(self):
        """position instantiation to be tested"""
        squ = Square(55, id=22, y=66, x=44)
        d_t = {'_Rectangle__height': 55, '_Rectangle__width': 55,
               '_Rectangle__x': 44, '_Rectangle__y': 66, 'id': 22}
        self.assertEqual(squ.__dict__, d_t)

    def test_e_id_inherited(self):
        """if id is inherited from base to be tested"""
        Base._Base__nb_of_objects = 33
        squ = Square(5)
        self.assertEqual(squ.id, 34)

    if __name__ == "__main__":
        unittest.main()
