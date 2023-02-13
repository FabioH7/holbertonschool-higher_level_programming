#!/usr/bin/python3
"""Module for base class"""


from models.base import Base


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


class Rectangle(Base):
    """Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        raise_exception(width=width, height=height, x=x, y=y)
        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        raise_exception(width=width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        raise_exception(height=height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        raise_exception(x=x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        raise_exception(y=y)
        self.__y = y

    def area(self):
        """returns area of function"""
        return self.__width * self.__height

    def display(self):
        """Prints rectangle"""
        for i in range(self.__y):
            print()
        for i in range(self.height):
            for j in range(self.__x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """returning string representation"""
        tostr = "[Rectangle] ({}) ".format(self.id)
        tostr += "{}/{} - ".format(self.__x, self.__y)
        tostr += "{}/{}".format(self.__width, self.__height)
        return tostr

    def update(self, *args):
        a = []
        for key in self.__dict__.keys():
            a.append(key)
        for i in range(len(args)):
            self.__dict__[a[i]] = args[i]
