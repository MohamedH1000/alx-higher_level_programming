#!/usr/bin/python3
"""
a module that is square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """rectangle that is inherited to this class"""

    def __init__(self, size):
        """a method that is called initialization"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)
