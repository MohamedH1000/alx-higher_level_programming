#!/usr/bin/python3
import unittest
import json
import sys
from io import StringIO
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class test_Rectangle(unittest.TestCase):
    """a test Rectangle class to be checked"""
    def setUp(self):
        """instantiates class , import modules"""
        Base._Base__nb_of_objects = 0

    def tearDown(self):
        """after each test method : cleans up"""
        pass

    def test_a_class(self):
        """class type called rectangle to be tested"""
        self.assertEqual(str(Rectangle), "<class 'models.rectangle.Rectangle'>")

    def test_b_inheritance(self):
        """test if rectangle inherit base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_d_instantiation_position(self):
        """test instantiation position"""
        rec = Rectangle(5, 6, 7, 8)
        d_t = {'_Rectangle__width': 5, '_Rectangle__height': 6,
               '_Rectangle__x': 7, '_Rectangle__y': 8,'id': 1}
        self.assertEqual(rec.__dict__, d_t)

        rec = Rectangle(2, 3, 4, 5, 198)
        d_t = {'_Rectangle__width': 2, '_Rectangle__height': 3,
               '_Rectangle__x': 4, '_Rectangle__y': 5, 'id': 198}
        self.assertEqual(rec.__dict__, d_t)

    def test_id(self):
        """a function to test and check the id"""
        Base._Base__nb_of_objects = 0
        rec1 = Rectangle(10, 5)
        self.assertIsNotNone(id(rec1))

    def test_init(self):
        """a function that test the proper instances created"""
        Base._Base__nb_of_objects = 0
        rec2 = Rectangle(10, 8)
        self.assertIsInstance(rec2, Rectangle)

    def test_num_of_objects(self):
        """a test that checks the numbe rof objects"""
        Base._Base__nb_of_objects = 0
        rec3 = Rectangle(7, 4, 8, 10)
        rec4 = Rectangle(5, 6)
        self.assertEqual(rec4.id, 2)

    def test_getter_and_setter(self):
        """a test that checks the numbe rof objects"""
        Base._Base__nb_of_objects = 0
        rec5 = Rectangle(7, 4, 8, 10)
        self.assertEqual(rec5.width, 7)
        self.assertEqual(rec5.height, 4)
        self.assertEqual(rec5.x, 8)
        self.assertEqual(rec5.y, 10)

    def test_area(self):
        """a function that tests area"""
        Base._Base__nb_of_objects = 0
        rec6 = Rectangle(8, 10)
        self.assertEqual(rec6.area(), rec6.width * rec6.height)

    def test_d_instantiation_keywords(self):
        """positional instantiation to be tested"""
        rec = Rectangle(30, 40, id = 77, y = 55, x = 66)
        d_t = {'_Rectangle__width': 30, '_Rectangle__height': 40,
               '_Rectangle__x': 66, '_Rectangle__y': 55, 'id': 77}
        self.assertEqual(rec.__dict__, d_t)

    def test_e_id_inheritance(self):
        """test if from base id get inherited"""
        Base._Base__nb_of_objects = 77
        rec = Rectangle(7, 3)
        self.assertEqual(rec.id, 78)

    if __name__ == "__main__":
        unittest.main()
