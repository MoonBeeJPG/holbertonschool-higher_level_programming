#!/usr/bin/python3
""" A function that read text file and prints it to stdout """


def read_file(filename=""):
    """ prototype defined """
    with open('my_file_0.txt', "r", encoding="utf-8") as i:
        print(i.read())
