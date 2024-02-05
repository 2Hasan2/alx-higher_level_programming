#!/usr/bin/python3

""" Module to create a class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle """
    def __init__(self, size):
        """ Method to initialize the square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
