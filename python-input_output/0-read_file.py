#!/usr/bin/python3
'''Opening and reading file module'''


def read_file(filename=""):
    '''ku ti kesh'''
    with open(filename, 'r', encoding="utf-8") as f:
        fr = f.read()
        print(fr)
