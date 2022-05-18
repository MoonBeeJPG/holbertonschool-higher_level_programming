#!/usr/bin/python3
"""A class"""


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

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __lt__(self, compare):
        return self.area() < compare.area()

    def __le__(self, compare):
        return self.area() <= compare.area()

    def __eq__(self, compare):
        return self.area() == comp.area()

    def __ne__(self, compare):
        return self.area() != comp.area()

    def __gt__(self, compare):
        return self.area() > comp.area()

    def __ge__(self, compare):
        return self.area() >= comp.area()
