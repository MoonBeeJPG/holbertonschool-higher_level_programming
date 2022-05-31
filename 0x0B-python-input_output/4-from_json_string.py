#!/usr/bin/python3
""" a fubnction that returns an object represented by a JSON string """
import json


def from_json_string(my_str):
    """ prototype defined """
    return json.loads(my_str)
