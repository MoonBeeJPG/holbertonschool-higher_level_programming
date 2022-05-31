#!/usr/bin/python3
""" A function that returns True if the object is an instance of a class
    that inherited from the specified class, otherwise False """


def inherits_from(obj, a_class):
    """ commit """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
