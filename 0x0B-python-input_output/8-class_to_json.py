#!/usr/bin/python3
""" a function that returns the dictionary description with simple 
    data structure """


def class_to_json(obj):
    """ prototype defined """
    return obj.__dict__
