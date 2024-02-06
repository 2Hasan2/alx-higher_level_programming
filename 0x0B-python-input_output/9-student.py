#!/usr/bin/python3


"""Student to JSON"""


class Student:
    """Student to JSON"""

    def __init__(self, first_name, last_name, age):
        """Student to JSON"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Student to JSON"""
        return self.__dict__
