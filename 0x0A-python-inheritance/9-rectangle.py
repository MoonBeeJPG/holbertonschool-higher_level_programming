#!/usr/bin/python3
""" a class Rectangle that inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle:
    """ commit """
    def __init__(self, width, height):
        """ commit """
        self.integer_validate("width", width)
        self.integer_validate("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ commit """
        return self.__width * self.__height

    def __str___(self):
        """ commit """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
