#!/usr/bin/python3
"""a square class to be defined"""


class Square:
    """
    prporties of square to be defined by this class

    Attributes:
        you can say size : 1 to be to the square
    """
    def __init__(self, size):
        """a new instances of square to be created.

        Args:
            size: the square size
        """
        self.__size = size
