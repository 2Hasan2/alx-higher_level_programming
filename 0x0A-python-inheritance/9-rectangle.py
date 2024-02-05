#!/usr/bin/python3


""" Module to create a class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Method to calculate the area """
        return self.__width * self.__height

    def __str__(self):
        """ Method to return a string representation of the object """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
