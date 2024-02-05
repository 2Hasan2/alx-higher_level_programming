#!/usr/bin/python3

""" Module to create a class """


class BaseGeometry:
    """ Class BaseGeometry """
    def area(self):
        """ Method to calculate the area """
        raise Exception("area() is not implemented")
