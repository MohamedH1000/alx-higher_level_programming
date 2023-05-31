#!/usr/bin/python3
"""a class square to be defined"""


class Square:
    """
    the properties of a square to be defined by that class

    Attributes:
        size: the square size (1 side)
    """
    def __init__(self, size=0):
        """new instances of a square to be created

        Args:
            size: square size (1 side)
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """an area of a square to be setermined

        Returns: the current square area to be returned
        """
        return self.__size ** 2

    @property
    def size(self):
        """a square of the size to be returned
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Size to has property setter

        Args:
            value (int): square size (1 side).

        Raises:
            TypeError: integer should be the size
            ValueError: its should be >= 0 (the size)
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
