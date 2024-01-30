#!/usr/bin/python3
"""Module 2-rectangle"""


class Rectangle:
    """Rectangle class defined by width and height"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width value if value is an int >= 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """Returns height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height value if value is an int >= 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width and self.__height:
            return (self.__width * 2) + (self.__height * 2)
        return 0
