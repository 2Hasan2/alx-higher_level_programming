#!/usr/bin/python3
"""this defines a class named rectangle"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle implements Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """adding width the getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """getter for the height"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("heigth must be > 0")

        self.__height = height

    @property
    def x(self):
        "getter for x"
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        """returns the area value"""
        return (self._width * self._height)

    def display(self):
        """dispaly the rectangle in stdout"""
        if self.__y != 0:
            print("\n" * self.__y, end="")
        for height in range(0, self.__height):
            print(" " * self.__x, end="")
            for width in range(0, self.__width):
                print("#", end="")
            print("")

    def _str_(self):
        """returns  task 6"""
        return (
                f"[{type(self)._name}] ({self.id}) {self.x}/{self._y}"
                f" - {self._width}/{self._height}"
                )

    def update(self, *args, **kwargs):
        """adding the new values to variables"""
        if len(args) == 0:
            for key, value in kwargs.items():
                self._setattr_(key, value)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """returns dicitionary represention"""
        return {'x': self._x, 'y': self._y, 'id': self.id,
                'height': self._height, 'width': self._width}
