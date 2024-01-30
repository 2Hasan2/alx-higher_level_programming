#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    num_instances = 0
    symbol = "#"

    def __init__(self, w=0, h=0):
        """Initialize a new Rectangle."""

        type(self).num_instances += 1
        self.w = w
        self.h = h

    @property
    def w(self):
        """Get/set the width of the Rectangle."""
        return self.__w

    @w.setter
    def w(self, v):
        if not isinstance(v, int):
            raise TypeError("w must be an integer")
        if v < 0:
            raise ValueError("w must be >= 0")
        self.__w = v

    @property
    def h(self):
        """Get/set the height of the Rectangle."""
        return self.__h

    @h.setter
    def h(self, v):
        if not isinstance(v, int):
            raise TypeError("h must be an integer")
        if v < 0:
            raise ValueError("h must be >= 0")
        self.__h = v

    def area(self):
        """Return the area of the Rectangle."""
        return self.__w * self.__h

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__w == 0 or self.__h == 0:
            return 0
        return (self.__w + self.__h) * 2

    @staticmethod
    def bigger_or_equal(r1, r2):
        """Return the Rectangle with the greater area.

        Args:
            r1 (Rectangle): The first Rectangle.
            r2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of r1 or r2 is not a Rectangle.
        """
        if not isinstance(r1, Rectangle):
            raise TypeError("r1 must be an instance of Rectangle")
        if not isinstance(r2, Rectangle):
            raise TypeError("r2 must be an instance of Rectangle")
        if r1.area() >= r2.area():
            return r1
        return r2

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__w == 0 or self.__h == 0:
            return ""

        rect = [str(self.symbol) * self.__w for _ in range(self.__h)]
        return "\n".join(rect)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self.__w}, {self.__h})"

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).num_instances -= 1
        print("Bye rectangle...")
