#!/usr/bin/python3
""" A function that read text file and prints it to stdout """


def read_file(filename=""):
    """ prototype defined """
    with open('my_file_0.txt', encoding="utf-8") as i:
        read_data = i.read()
        print(read_data, end="")
