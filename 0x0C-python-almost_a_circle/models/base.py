#!/usr/bin/python3
""" Base of all other classes in the project """
import json


class Base:
    """ creting class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init attributes """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returning json string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes json string representation of list_objs to a file """
        file_name = cls.__name__ + ".json"
        if list_objs is None:
            lists = "[]"
        else:
            lists = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])
        with open(file_name, "w") as MyFile:
            MyFile.write(lists)

    def from_json_string(json_string):
        """ returning list of json string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
