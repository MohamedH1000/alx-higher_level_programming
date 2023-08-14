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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

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
        ttl = ""
        for a in range(0, self.height):
            for b in range(0, self.width):
                try:
                    ttl += str(self.print_symbol)
                except Exception:
                    ttl += type(self).print_symbol
            if a is not self.__height - 1:
                ttl += "\n"
        return ttl

    def __repr__(self):
        strn = "Rectangle("
        strn += str(self.width)
        strn += ", " + str(self.height) + ")"
        return strn

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
