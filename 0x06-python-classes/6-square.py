#!/usr/bin/python3
"""a class square to be defined"""


class Square:
    """
    the properties of a square to be defined by that class

    Attributes:
        size: the square size (1 side)
    """
    def __init__(self, size=0, position=(0, 0)):
        """new instances of a square to be created

        Args:
            size: square size (1 side)
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """position of a square to be returned
        """
        return self.__position

    @position.setter
    def position(self, value):
        """position to has property setter

        Args:
            value (tuple): the square position

        Raises:
            TypeError: 2 positive integers must be a tuple in position
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """the square with the character # to printed in stdout
        """

        if self.__size == 0:
            print()
        else:
            for b in range(self.__position[1]):
                print()
            for a in range(self.__size):
                for c in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))
