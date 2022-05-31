#!/usr/bin/python3
""" a function that writes a string to a text file and returns
    the number of characters written """


def write_file(filename="", text=""):
    """ prototype defined """
    with open(filename, mode="w") as MyFile:
        return MyFile.write(text)
