#!/usr/bin/python3
""" A function that return True if the object is an instance of, or if the
    object is an instance of a class that inherited from, the specified class,
    otherwise, False """


def is_kind_of_class(obj, a_class):
    """ comment """
    return (isinstance(obj, a_class))
