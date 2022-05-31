#!/usr/bin/python3
""" a function that returns the dictionary description with simple 
    data structure """


def class_to_json(obj):
    """ prototype defined """
    my_dict = {}
    with open(obj, "w") as f:
        return str(my_dict.dump(f))
