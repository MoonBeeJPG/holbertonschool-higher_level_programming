#!/usr/bin/python3
"""A class Square that defines a square based on 6-squared.py"""


class Square:
    """square class, empty"""
    def __init__(self, size=0, position=(0, 0)):
        """init the square instance"""
        self.size = size
        self.position = position

    def area(self):
        """returns the area"""
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (len(value) != 2 or not isinstance(value, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not isinstance(value[0], int) or not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print("")
        else:
            if self.__position[1] > 0:
                for i in range(self.__position[1]):
                    print("")
            for j in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def square_cp(self):
        """prints the square again"""
        cp = ""
        if self.__size == 0:
            cp += "\n"
        else:
            if self.__position[1] > 0:
                for i in range(self.__position[1]):
                    cp += "\n"
            for j in range(self.__size):
                cp += " " * self.__position[0] + "#" * self.__size + "\n"
        return cp[:-1]
