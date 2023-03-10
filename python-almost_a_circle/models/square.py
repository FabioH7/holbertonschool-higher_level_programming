#!/usr/bin/python3
"""Module for square class"""


from models.rectangle import Rectangle


def raise_exception(**kwargs):
    """Raises exceptions for rectangle class"""
    sides = ['width', 'height']
    ls = ['x', 'y']
    for key, value in kwargs.items():
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(key))
        if key in sides and value <= 0:
            raise ValueError("{} must be > 0".format(key))
        if key in ls and value < 0:
            raise ValueError("{} must be >= 0".format(key))


class Square(Rectangle):
    """Square class, inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        tostr = "[Square] ({}) ".format(self.id)
        tostr += "{}/{} - ".format(self.x, self.y)
        tostr += "{}".format(self.size)
        return tostr

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates square object attributes"""
        att = ['id', 'size', 'x', 'y']
        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, att[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of square class"""
        ls = ['id', 'size', 'x', 'y']
        toDict = {}
        for item in ls:
            toDict[item] = getattr(self, item)
        return toDict
