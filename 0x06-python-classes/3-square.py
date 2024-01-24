#!/usr/bin/python3

"""Square class with size attribute"""


class Square:
    """Square class with size attribute"""
    def __init__(self, size=0):
        """Initializes Square with size attribute"""
        self.__size = size

    def area(self):
        """Returns area of Square instance"""
        return self.__size ** 2
