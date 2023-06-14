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

    def to_json(self, attrs=None):
        '''with filters a dictionary to be retrieved.'''
        if type(attrs) is list and all([type(a) == str for a in attrs]):
            return {c: f for c, f in self.__dict__.items() if c in attrs}
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        '''json attributed to be loaded'''
        for akey, value in json.items():
            self.__dict__[akey] = value
