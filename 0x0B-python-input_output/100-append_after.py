#!/usr/bin/python3
""" a function that inserts a line of text to a file, after each line
    containing a specific string """


def append_after(filename="", search_string="", new_string=""):
    """ prototype defined """
    with open(filename, "r") as MyList:
        
