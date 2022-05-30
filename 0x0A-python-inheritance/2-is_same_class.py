#!/usr/bin/python3
""" A function that return True if the object is exactly an instance
    of the specified class. otherwise False """


def is_same_class(obj, a_class):
    """ commit """
    return type(obj) == a_class
