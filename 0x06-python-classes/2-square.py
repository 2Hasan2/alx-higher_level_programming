#!/usr/bin/python3
"""Square class with size attribute"""


class Square:
    """Square class with size attribute"""
    def __init__(self, size=0):
        """Initializes Square with size attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size
