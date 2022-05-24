#!/usr/bin/python3
""" A function that adds 2 integers """


def add_integer(a, b=98):
    """ check if the parameters are int otherwise return the addition """
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
