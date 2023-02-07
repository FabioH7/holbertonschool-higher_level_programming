#!/usr/bin/python3
"""Module for a list subclass"""


class MyList(list):
    '''Prints a sorted list'''
    def print_sorted(self):
        ls = self.copy()
        ls.sort()
        print(ls)
        return ls
