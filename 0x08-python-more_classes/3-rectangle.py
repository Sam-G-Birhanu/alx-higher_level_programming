#!/usr/bin/python3
""" this module contains a class named Rectangle """


class Rectangle:
    """ this class defines a rectangle """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        self.Area = self.__width * self.__height
        return self.Area

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        self.Perimeter = (2 * self.__width) + (2 * self.__height)
        return self.Perimeter
    def __str__(self):
        
        p = []
        for i in range(self.height):
            tp = []
            for j in range(self.width):
                tp.append("#")
            p.append("".join(tp))
        return "\n".join(p)
