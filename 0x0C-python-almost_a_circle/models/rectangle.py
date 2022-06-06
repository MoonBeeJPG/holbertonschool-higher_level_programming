#!/usr/bin/python3
""" a class Rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ creating class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init attributes """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """ comment """
        return self.__height

    @height.setter
    def height(self, height):
        """ setting height """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def width(self):
        """ comment """
        return self.__width

    @width.setter
    def width(self, width):
        """ setting width """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def x(self):
        """ comment """
        return self.__x

    @x.setter
    def x(self, x):
        """ setting x """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ comment """
        return self.__y

    @y.setter
    def y(self, y):
        """ setting y """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ returns area of rectangle """
        return self.height * self.width

    def display(self):
        """ display rectangle """
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """ return str """
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ update arguments """
        arguments = len(args)
        if arguments > 0:
            self.id = args[0]
        if arguments > 1:
            self.width = args[1]
        if arguments > 2:
            self.height = args[2]
        if arguments > 3:
            self.x = args[3]
        if arguments > 4:
            self.y = args[4]
        if arguments == 0:
            for key, value in kwargs.items():
                exec("self.{} = {}".format(key, value))

    def to_dictionary(self):
        """ returns dictionary """
        dictionary = {'x': {}, 'y': {}, 'id': {},'height': {}, 'width': {}}.\
        format(self.x, self.y, self.id, self.height, self.width)
        return dictionary
