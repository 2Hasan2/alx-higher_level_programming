#!/usr/bin/python3

""" Module to create a class """


class BaseGeometry:
    """ Class BaseGeometry """
    def area(self):
        """ Method to calculate the area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method to validate an integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
