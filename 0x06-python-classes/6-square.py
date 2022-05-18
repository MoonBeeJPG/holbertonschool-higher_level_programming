#!/usr/bin/python3
"""A class Square that defines a square based on 3-squared.py"""


class Square:
    """square class, empty"""
    """define the private __size attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """define the init for the square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size
            self.position = position

    def area(self):
        """define and return the area of the square"""
        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        """define size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """define position"""
        return self.__position

    @position.setter
    def position(self, value):
        """define position"""
        if (len(value) != 2 or type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 posiive integers")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 posiive integers")
        elif (type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 posiive integers")
        else:
            self.__position = value

    def my_print(self):
        """define my_print"""
        if self.__size == 0:
            print("")
        else:
            if self.__position[1] > 0:
                for i in range(self.__position[1]):
                    print()
            for j in range(self.__size):
                print(" " * self.position[0] + "#" * self.__size)
