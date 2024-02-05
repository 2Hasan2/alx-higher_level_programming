#!/usr/bin/python3

""" Module to add an attribute to a class """


def add_attribute(obj, attribute, value):
    """ Function to add an attribute to a class """
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
