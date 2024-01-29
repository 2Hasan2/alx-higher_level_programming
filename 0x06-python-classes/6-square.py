#!/usr/bin/python3

"""Square class with size attribute"""


class Square:
    """Square class with size attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes Square with size attribute"""
        self.__size = size
        self.__position = position

    def area(self):
        """Returns area of Square instance"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter for position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position attribute"""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not isinstance(value[0], int) or not isinstance(value[1], int) \
           or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Prints square with # character"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
