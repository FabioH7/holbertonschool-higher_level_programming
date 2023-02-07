#!/usr/bin/python3
"""module to write in file"""


def append_write(filename="", text=""):
    '''Function that writes text inside file'''
    with open(filename, 'a', encoding="utf-8") as f:
        count = f.write(text)
    return count
