#!/usr/bin/python3
""" this module contains a class named Rectangle """


class Rectangle:
    """ this class defines a rectangle """
    
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return ""
        p = []
        self.print_symbol = str(self.print_symbol)
        for i in range(self.height):
            tp = []
            for j in range(self.width):
                tp.append(self.print_symbol)
            p.append("".join(tp))
        return "\n".join(p)
    
    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
    
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

    @classmethod        
    def square(cls, size=0):
        new_obj = Rectangle(size, size)
        return new_obj
