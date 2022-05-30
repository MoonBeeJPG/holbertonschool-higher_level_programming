#!/usr/bin/python3
""" A class BaseGeometry based on 6-base_geometry.py """


def BaseGeometry:
    """ comment """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(slef, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
