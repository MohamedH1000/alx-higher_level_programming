#!/usr/bin/python3
"""
    student class for module
"""


class Student:
    """
        A class students that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
            instant student initialization
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            student to retieve a dictionary representation
        """
        if attr is not None:
            result = {a: self.__dict__[a] for a in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__
