#!/usr/bin/python3
""" a function that adds a new attribute to an object if its possible """


def add_attribute(obj, name, value):
    """ commit """
    if ('__dict__' in dir(obj)):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
