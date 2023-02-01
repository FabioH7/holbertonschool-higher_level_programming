#!/usr/bin/python3
"""Say my name Module """


def say_my_name(first_name, last_name=""):
    """Gets a name and a surname if provided and prints the full name"""
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
