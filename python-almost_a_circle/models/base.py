#!/usr/bin/python3
"""Module for base class"""


import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns string repr of dict"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves dictionary repr to json file"""
        filename = '{}.json'.format(cls.__name__)
        ls = []
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write(json.dumps(ls))
            else:
                for elem in list_objs:
                    class_dict = cls.to_dictionary(elem)
                    ls.append(class_dict)
                f.write(Base.to_json_string(ls))

    @staticmethod
    def from_json_string(json_string):
        """Turns a string to a python object"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        new_obj = cls(1, 2)
        new_obj.update(**dictionary)
        return new_obj
