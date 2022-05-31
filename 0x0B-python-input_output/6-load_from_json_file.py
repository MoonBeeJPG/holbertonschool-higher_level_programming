#!/usr/bin/python3
""" a function that creates an object from JSON file """
import json


def load_from_json_file(filename):
    """ prototype defined """
    with open(filename, mode="r") as MyFile:
        return json.load(MyFile)
