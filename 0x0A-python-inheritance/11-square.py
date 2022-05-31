#!/usr/bin/python3
"""  a class Square that inherits from Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


def Square(Rectangle):
    """ comment """
    def __init__(self, size):
        """ comment """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ area """
        return self.__size ** 2

    def __str__(self):
        """ print """
        return f"[square] {self.__size}/{self.__size}"
