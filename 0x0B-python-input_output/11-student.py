#!/usr/bin/python3
""" a class Student that defines a strudent by 10-student.py """


class Student:
    """ class defined """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, str):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            self.__dict__[key] = value
