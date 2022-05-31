#!/usr/bin/python3
""" a function that writes a string to a text file and returns
    the number of characters written """


def write_filename(filename="", text=""):
    """ prototype defined """
    with open('my_first_file.txt', encoding="utf-8") as MyFile:
        MyFile.write("This School is so cool!")
