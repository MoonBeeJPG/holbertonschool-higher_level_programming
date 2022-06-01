#!/usr/bin/python3
""" a function that writes an object to a text file, using JSON
    representation """
import json


def save_to_json_file(my_obj, filename):
    """ prototype defined """
    with open(filename, "w") as MyFile:
        return json.dump(my_obj, MyFile)
