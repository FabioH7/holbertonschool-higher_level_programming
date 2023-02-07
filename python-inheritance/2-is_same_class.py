#!/usr/bin/python3
'''Module for objects and classes'''


def is_same_class(obj, a_class):
    '''Finds if an object is an instance of a class'''
    if a_class is object:
        return False
    return isinstance(obj, a_class)
