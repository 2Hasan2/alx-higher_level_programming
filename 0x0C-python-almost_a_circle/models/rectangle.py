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
        """validates the value"""
        self.validator("width", width)
        self.__width = width

    @property
    def height(self):
        """getter for the height"""
        return self.__height

    @height.setter
    def height(self, height):
        self.validator("height", height)
        self.__height = height


    def validator(self, name, value):
        """validates the value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0 and (name == "width" or name == "height"):
            raise ValueError(f"{name} must be > 0")
        if value < 0 and (name == "x" or name == "y"):
            raise ValueError(f"{name} must be >= 0")

    @property
    def x(self):
        "getter for x"
        return self.__x

    @x.setter
    def x(self, x):
        """validates the value"""
        self.validator("x", x)
        self.__x = x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        self.validator("y", y)
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
