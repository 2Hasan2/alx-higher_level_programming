#!/usr/bin/python3
"""Rectangle module."""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Get the x of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x of the Rectangle."""
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Get the y of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y of the Rectangle."""
        self.integer_validator("y", value)
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle with the character #."""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the string representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the attributes of the Rectangle."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    # Errors Handling
    def integer_validator(self, name, value):
        """Validate the value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name in ("width", "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if name in ("x", "y") and value < 0:
            raise ValueError("{} must be >= 0".format(name))
