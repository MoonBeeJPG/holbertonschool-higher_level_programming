#!/usr/bin/python3
""" a class Student that defines a student by 9-student.py """


class Student:
    """ class defined """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        if isinstance(attr, str):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        else:
            return self.__dict__
