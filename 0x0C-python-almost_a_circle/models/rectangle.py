#!/usr/bin/python3
"""Rectangle module."""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        self.__is_validate_positive_integer(value, "width")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
        self.__is_validate_positive_integer(value, "width")
        self.__height = value

    @property
    def x(self):
        """Get the x of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x of the Rectangle."""
        self.__is_validate_positive_integer_or_zero(value, "x")
        self.__x = value

    @property
    def y(self):
        """Get the y of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y of the Rectangle."""
        self.__is_validate_positive_integer_or_zero(value, "y")
        self.__y = value

    # Errors Handling
    def __is_validate_integer(self, value, attribute):
        """Validate if value is an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")

    def __is_validate_positive_integer(self, value, attribute):
        """Validate if value is a positive integer."""
        self.__is_validate_integer(value, attribute)
        if value <= 0:
            raise ValueError(f"{attribute} must be > 0")

    def __is_validate_positive_integer_or_zero(self, value, attribute):
        """Validate if value is a positive integer or zero."""
        self.__is_validate_integer(value, attribute)
        if value < 0:
            raise ValueError(f"{attribute} must be >= 0")
