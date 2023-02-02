#!/usr/bin/python3
"""Module for rectangle class"""


class Rectangle:
    """Empty rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        perim = (self.__height * 2) + (self.__width * 2)
        return perim

    def __str__(self):
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            if i + 1 != self.__height:
                string += '\n'
        return string

    def __repr__(self):
        a = 'Rectangle('
        return a + str(self.__width) + ', ' + str(self.__height) + ')'

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @classmethod
    def bigger_or_equal(cls, rect_1, rect_2):
        if type(rect_1) is not cls:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not cls:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
