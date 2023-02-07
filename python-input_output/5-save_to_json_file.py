#!/usr/bin/python3
"""module to write in file"""


import json


def save_to_json_file(my_obj, filename):
    '''Writes in json string format'''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
