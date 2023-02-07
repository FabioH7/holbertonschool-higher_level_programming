#!/usr/bin/python3
'''Module for inherited classes'''


def inherits_from(obj, a_class):
    '''Gets all the inherited classes of an object'''
    if isinstance(obj, a_class):
        if obj.__class__ is a_class:
            return False
        return True
    return False
