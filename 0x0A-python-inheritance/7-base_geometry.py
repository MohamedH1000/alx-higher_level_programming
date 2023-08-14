#!/usr/bin/python3
"""
a module class
"""


class BaseGeometry:
    """a class that is called geometry"""

    def area(self):
        """area is not implemented to raise exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """an integer to be checked if its value"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
