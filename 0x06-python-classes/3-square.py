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
