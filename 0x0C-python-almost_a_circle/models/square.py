#!/usr/bin/python3
"""square class module for this file"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square for this file"""

    def __init__(self, size, x=0, y=0, id=None):
        """this is an initialized contruction method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """this square info to be returned by a string"""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """square size to be determined"""
        return self.width

    @size.setter
    def size(self, value):
        self.__width = value
        self.__height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """instant attributes via args to be updated by internal method"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.__x = x
        if y is not None:
            self.__y = y

    def update(self, *args, **kwargs):
        """no keyword args and keyword args updates instant attributes"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """this class dictionary representation to be returned"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
