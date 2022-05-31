#!/usr/bin/python3
"""module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square defined"""

    def __init__(self, size):
        """initialize the size"""
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """defined area"""
        return self.__size ** 2

    def __str__(self):
        """print"""
        return f"[Square] {self.__size}/{self.__size}"
