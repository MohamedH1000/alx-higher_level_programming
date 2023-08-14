#!/usr/bin/python3
"""
a module class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass that is rectangle"""

    def __init__(self, width, height):
        """method called initialization"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculate the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """a method that is called print"""
        return "[{}] {}/{}".format(__class__.__name__,
                                   self.__width, self.__height)
