#!/usr/bin/python3
""" A function that appends a string at the end of a text file
    and returns the number of characters added """


def append_write(filename="", text=""):
    """ prototype defined """
    with open(filename, mode="a") as MyFile:
       return MyFile.write(text)
