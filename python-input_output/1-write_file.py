#!/usr/bin/python3
"""module to write in file"""


def write_file(filename="", text=""):
    '''Function that writes text inside file'''
    with open(filename, 'w', encoding="utf-8") as f:
        count = f.write(text)
    return count
