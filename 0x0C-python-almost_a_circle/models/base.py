#!/usr/bin/python3
""" Base of all other classes in the project """
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """ returning list of json string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returning an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returning list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as MyFile:
                return [cls.create(**obj) for obj
                        in cls.from_json_string(MyFile.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes and deserialized in CSV """
        if list_objs:
            filename = cls.__name__ + ".cvs"
            with open(filename, "w") as MyFile:
                if "Rectangle" in filename:
                    fields = ["id", "width", "height", "x", "y"]
                elif "Square" in filename:
                    fields = ["id", "size", "x", "y"]
                writing = csv.DictWriter(MyFile, fieldnames=fields)
                writing.writeheader()
                for obj in list_objs:
                    writing.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ serializes and deserialized in CSV """
        filename = cls.__name__ + ".csv"
        if (filename):
            if "Rectangle" in filename:
                fields = ["id", "width", "height", "x", "y"]
            elif "Square" in filename:
                fields = ["id", "size", "x", "y"]
            obj_list = []
            with open(filename, "r") as MyFile:
                reading = csv.DictReader(MyFile)
                for i in reading:
                    if len(fields) == 4:
                        instance = cls(1)
                    elif len(fields) == 5:
                        instance = cls(1, 1)
                    for j, k in enumerate(i):
                        setattr(instance, fields[j], int(i[k]))
                    obj_list.append(instance)
                return obj_list
