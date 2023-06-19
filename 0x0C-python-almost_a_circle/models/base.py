#!/usr/bin/python3
"""We create a module for base class"""
import csv
import turtle
from json import dumps, loads


class Base:
    """A class that represent a base of our project"""

    __nb_of_objects = 0

    def __init__(self, id=None):
        """this is a constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_of_objects += 1
            self.id = Base.__nb_of_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to create a dictionery and to be quite rightly and longer"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """to disconnect a dictionary"""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save a conection of objects to file"""
        if list_objs is not None:
            list_objs = [a.to_dictionary() for a in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as F:
            F.write(cls.to_json_string(list_objs))

    @classmethod
    def load_from_file(cls):
        """to load a string from a file and disconnect it"""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as File:
            return [cls.create(**a) for a in cls.from_json_string(File.read())]

    @classmethod
    def create(cls, **dictionary):
        """From dictionary instance to be loaded"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            n = Rectangle(1, 1)
        elif cls is Square:
            n = Square(1)
        else:
            n = None
        n.update(**dictionary)
        return n

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """an object to csv file to be saved"""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[a.id, a.width, a.height, a.x, a.y] for a in list_objs]
            else:
                list_objs = [[a.id, a.size, a.x, a.y] for a in list_objs]
                with open('{}.csv'.format(cls.__name__), 'w', newline='', encoding='utf-8') as F:
                    wr = csv.writer(F)
                    wr.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """object to csv file to be loaded"""
        from models.rectangle import Rectangle
        from models.square import Square
        rt = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='', encoding='utf-8') as File:
            rea = csv.reader(File)
            for r in rea:
                r = [int(ow) for ow in r]
                if cls is Rectangle:
                    lo = {"id": r[0], "width": r[1], "height": r[2], "i": r[3], "j": r[4]}
                else:
                    lo = {"id": r[0], "size": r[1], "i": r[2], "j": r[3]}
                rt.append(cls.create(**lo))
        return rt

    @staticmethod
    def draw(list_rectangles, list_squares):
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for a in list_rectangles + list_squares:
            tur = turtle.Turtle()
            tur.pensize(1)
            tur.pendown()
            tur.penup()
            tur.color((randrange(255), randrange(255), randrange(255)))
            tur.setpos((a.x + tur.pos()[0], a.y - tur.pos()[1]))
            tur.pensize(10)
            tur.forward(a.width)
            tur.left(90)
            tur.forward(a.height)
            tur.left(90)
            tur.forward(a.width)
            tur.left(90)
            tur.forward(a.height)
            tur.left(90)
            tur.end_fill()

        time.sleep(5)
