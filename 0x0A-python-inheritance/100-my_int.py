#!/usr/bin/python3
""" A class MyInt that inherits from int """


class MyInt:
    """ class """
    def __init__(self, myint):
        """ comment """
        self.myint = myint

    def __eq__(a1, b2):
        """ different """
        return a1.myint != b2

    def __ne__(a1, b2):
        """ compare """
        return a1.myint == b2
