#!/usr/bin/python3
"""Module for square class"""


Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    '''Subclass of Rectangle named square'''
    def __init__(self, size):
        '''Initialisation of square object '''
        BaseGeometry.integer_validator(self, 'size', size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        '''Returns area of square'''
        return self.__size ** 2

    def __str__(self):
        to_str = '[Square] '
        to_str += str(self.__size) + '/' + str(self.__size)
        return to_str
