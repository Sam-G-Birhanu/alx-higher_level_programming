#!/usr/bin/python3
""" this module contains a class named Rectangle """


class Rectangle:
    """ this class defines a rectangle """

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        else:
            self._width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        else:
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
