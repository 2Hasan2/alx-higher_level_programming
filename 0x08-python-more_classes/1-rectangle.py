#!/usr/bin/python3

"""Rectangle class"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """__init__ method.

        Args:
            width (int): integer width
            height (int): integer height

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width: returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width: sets width

        Args:
            value (int): integer value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        """height: returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height: sets height

        Args:
            value (int): integer value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value
