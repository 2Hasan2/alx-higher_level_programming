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

    @property
    def size(self):
        """Getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value
