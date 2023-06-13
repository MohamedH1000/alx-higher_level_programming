#!/usr/bin/python3
"""
a module class
"""


class BaseGeometry:
    """a class that is called geometry"""

    def area(self):
        """area is not implemented to raise exception"""
        raise Exception('area() is not implemented')
