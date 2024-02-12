#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv


class Base:
    """Base model."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        import json
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                list_dicts = Base.from_json_string(file.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV string representation of list_objs to a file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("")
            else:
                if cls.__name__ == "Rectangle":
                    [file.write("{},{},{},{},{}\n".format(
                        obj.id, obj.width, obj.height, obj.x, obj.y))
                        for obj in list_objs]
                elif cls.__name__ == "Square":
                    [file.write("{},{},{},{}\n".format(
                        obj.id, obj.size, obj.x, obj.y))
                        for obj in list_objs]

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                if cls.__name__ == "Rectangle":
                    list_objs = csv.reader(file, delimiter=',', quotechar='"')
                    return [cls.create(id=int(r[0]), width=int(r[1]),
                            height=int(r[2]),
                            x=int(r[3]), y=int(r[4])) for r in list_objs]
                elif cls.__name__ == "Square":
                    list_objs = csv.reader(file, delimiter=',', quotechar='"')
                    return [cls.create(id=int(r[0]), size=int(r[1]),
                            x=int(r[2]),
                            y=int(r[3])) for r in list_objs]
        except IOError:
            return []
        
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using the turtle module."""
        import turtle
        import random

        turtle.bgcolor("white")
        turtle.title("Rectangles and Squares")
        turtle.shape("turtle")

        for rect in list_rectangles:
            turtle.penup()
            turtle.color("black")
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            turtle.forward(rect.width)
            turtle.left(90)
            turtle.forward(rect.height)
            turtle.left(90)
            turtle.forward(rect.width)
            turtle.left(90)
            turtle.forward(rect.height)
            turtle.left(90)

        for square in list_squares:
            turtle.penup()
            turtle.color("black")
            turtle.goto(square.x, square.y)
            turtle.pendown()
