#!/usr/bin/python3
"""Module for square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)
        self.size = size

    def __str__(self):
        tostr = "[Square] ({}) ".format(self.id)
        tostr += "{}/{} - ".format(self.x, self.y)
        tostr += "{}".format(self.size)
        return tostr
