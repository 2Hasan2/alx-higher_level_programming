#!/usr/bin/python3


""" Module to create a class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Method to initialize the rectangle """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Method to calculate the area """
        return self.__width * self.__height

    def __str__(self):
        """ Method to print the rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
