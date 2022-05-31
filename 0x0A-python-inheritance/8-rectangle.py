#!/usr/bin/python3
""" a class Rectangle that inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle:
    """ comment """
    def __init__(self, width, height):
        """ comment """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
