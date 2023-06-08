#!/usr/bin/python3
""" a rectangle module """


class Rectangle():
    """ a rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """ a new value to be set to the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ when str or print is called this
        define a str permission
        """
        strn = ""
        if self.width == 0 or self.height == 0:
            return strn

        for a in range(0, self.height):
            for b in range(0, self.width):
                strn += '#'
            if a != self.height - 1:
                strn += '\n'
        return strn

    def __repr__(self):
        strn = "Rectangle("
        strn += str(self.width)
        strn += ", " + str(self.height) + ")"
        return strn

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
