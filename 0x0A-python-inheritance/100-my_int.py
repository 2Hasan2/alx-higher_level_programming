#!/usr/bin/python3

""" Module to create a class """


class MyInt(int):
    """ Class MyInt """
    def __eq__(self, other):
        """ Method to check if two objects are equal """
        return int(self) != int(other)

    def __ne__(self, other):
        """ Method to check if two objects are not equal """
        return int(self) == int(other)
