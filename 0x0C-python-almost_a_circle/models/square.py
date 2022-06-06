#!/usr/bin/python3
""" a class Square that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ creating class """
    def __init__(self, size, x=0, y=0, id=None):
        """ init attributes """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ comment """
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ comment """
        return self.height

    @size.setter
    def size(self, size):
        """ setting to size """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ updating arguments """
        arguments = len(args)
        if arguments > 0:
            self.id = args[0]
        if arguments > 1:
            self.width = args[1]
            self.height = args[1]
        if arguments > 2:
            self.x = args[2]
        if arguments > 3:
            self.y = args[3]
        if arguments == 0:
            for key, value in kwargs.items():
                exec("self.{} = {}".format(key, value))

    def to_dictinary(self):
        """ return dictionary """
        dictionary = {"id": self.id, "size": self.width, "x": self.x,
                      "y": self.y}
        return dictionary
