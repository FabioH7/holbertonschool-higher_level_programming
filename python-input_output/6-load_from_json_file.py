#!/usr/bin/python3
"""module to write in file"""


import json


def load_from_json_file(filename):
    '''Writes in json string format'''
    with open(filename, 'r', encoding='utf-8') as f:
        read = f.read()
    return json.loads(read)
