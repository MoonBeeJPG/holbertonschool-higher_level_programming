#!/usr/bin/python3
"""Implement a rectangle class from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class based on Basegeometry"""

    def __init__(self, width, height):
        """we initialize"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
