#!/usr/bin/python3
""" a function that adds a new attribute to an object if its possible """


def add_attribute(obj, name, value):
    """ commit """
    if not isinstance(name, str):
        raise TypeError("can't add new attribute")
    try:
        exec(f"obj.{name} = value")
    except:
        raise TypeError("can't add new attribute")
