#!/usr/bin/python3
"""A class Square that defines a square based on 2-squared.py"""


class Square:
    """square class, empty"""
    __size = None
    """define the private __size attribute"""
    def __init__(self, size=0):
        """define the init for the square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    def area(self):
        """define and return the area of the square"""
        return (self.__size ** 2)
