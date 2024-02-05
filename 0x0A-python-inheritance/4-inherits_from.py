#!/usr/bin/python3

""" Module to check if an object is an instance of a class """


def inherits_from(obj, a_class):
    """ Function to check if an object is an instance of a class """
    return isinstance(obj, a_class) and type(obj) is not a_class
