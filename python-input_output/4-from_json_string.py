#!/usr/bin/python3
"""module to write in file"""


import json


def from_json_string(my_obj):
    '''Writes in json string format'''
    return json.loads(my_obj)
