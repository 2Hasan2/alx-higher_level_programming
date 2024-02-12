#!/usr/bin/python3
"""Square module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get size """
        return self.size

    @size.setter
    def size(self, value):
        """ set size """
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Update the Square."""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.size = arg
                elif i == 1:
                    self.x = arg
                elif i == 2:
                    self.y = arg
                elif i == 3:
                    self.id = arg
        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                elif key == "id":
                    self.id = value
