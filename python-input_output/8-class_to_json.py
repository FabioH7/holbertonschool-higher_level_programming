#!/usr/bin/python3
"""Class to json Module"""


import json


def class_to_json(obj):
    d = {}
    for attr, value in obj.__dict__.items():
        d[attr] = value
    return d
