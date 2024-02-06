#!/usr/bin/python3


"""Student to JSON"""


class Student:
    """Student to JSON"""

    def __init__(self, first_name, last_name, age):
        """Student to JSON"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Student to JSON"""
        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Reload from JSON"""
        for k, v in json.items():
            setattr(self, k, v)
