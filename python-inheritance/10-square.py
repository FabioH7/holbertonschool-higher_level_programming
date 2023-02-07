#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Module for square class"""


class Square(Rectangle):
    '''Subclass of Rectangle named square'''
    def __init__(self, size):
        BaseGeometry.integer_validator(self, 'size', size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2
