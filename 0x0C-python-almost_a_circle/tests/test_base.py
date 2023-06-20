#!/usr/bin/python3
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Testbase class to be tested by this class"""
    def test_id(self):
        """to test if the id is true or not"""
        Base._Base__nb_of_objects = 0
        p1 = Base()
        self.assertIsNotNone(id(p1))

    def test_init(self):
        """a test that check the instances"""
        Base._Base__nb_of_objects = 0
        p2 = Base()
        self.assertIsInstance(p2, Base)

    def test_the_numbofobj(self):
        """a test the number of objects to be checked"""
        Base._Base__nb_of_objects = 0
        p3 = Base()
        self.assertEqual(p3.id, 1)

    def test_to_json_string(self):
        """a test that to json string to be checked"""
        Base._Base__nb_of_objects = 0
        rec1 = Rectangle(8, 5, 3, 7)
        rec2 = Rectangle(3,5)
        to_dict = [rec1.to_dictionary(), rec2.to_dictionary()]
        Base.save_to_file([rec1, rec2])
        with open("Base.json", "r") as File:
            a_list_of_dict = json.loads(File.read())
        self.assertTrue(to_dict == a_list_of_dict)

    def test_save_to_file(self):
        """test the save to file to be checked"""
        Base._Base__nb_of_objects = 0
        rec1 = Rectangle(5, 7, 10, 2)
        rec2 = Rectangle(6, 9)
        to_dict = [rec1.to_dictionary(), rec2.to_dictionary()]
        Base.save_to_file([rec1, rec2])
        with open("Base.json", "r") as File:
            a_list_of_dict = json.loads(File.read())
        self.assertTrue(to_dict == a_list_of_dict)

    def test_from_json_string(self):
        """a test from json string to be checked"""
        Base._Base__nb_of_objects = 0
        input_list = [{'id': 53, 'width': 17, 'height': 14},
                      {'id': 67, 'width': 95, 'height': 20}]
        json_input_list = Base.to_json_string(input_list)
        output_list = Base.from_json_string(json_input_list)
        self.assertTrue(input_list == output_list)

    def test_create_check(self):
        """a test of this creation to be checked"""
        Base._Base__nb_of_objects = 0
        rec1 = Rectangle(5, 7, 2)
        rec1_dict = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dict)
        self.assertFalse(rec1 is rec2)
        self.assertFalse(rec1 == rec2)

    def test_load_from_file(self):
        """a test the checks the load from a file"""
        Base._Base__nb_of_objects = 0
        rec1 = Rectangle(4, 5, 8, 9)
        rec2 = Rectangle(1, 4)
        input_list_Rectangles = [rec1, rec2]
        Rectangle.save_to_file(input_list_Rectangles)
        output_list_Rectangles = Rectangle.load_from_file()
        self.assertTrue(type(output_list_Rectangles) == list)
        for r in input_list_Rectangles:
            self.assertTrue(isinstance(r, Rectangle))
        for r in output_list_Rectangles:
            self.assertTrue(isinstance(r, Rectangle))
        squ1 = Square(8)
        squ2 = Square(5, 4, 2)
        input_list_Squares = [squ1, squ2]
        Square.save_to_file(input_list_Squares)
        output_list_Squares = Square.load_from_file()
        self.assertTrue(type(output_list_Squares) == list)
        for s in input_list_Squares:
            self.assertTrue(isinstance(s, Square))
        for s in output_list_Squares:
            self.assertTrue(isinstance(s, Square))

    if __name__ == "__main__":
        unittest.main()
