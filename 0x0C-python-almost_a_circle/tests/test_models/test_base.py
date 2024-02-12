#!/usr/bin/python3
"""Defines unittests for base.py. """

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseToJsonString(unittest.TestCase):
    """Tests the to_json_string method of the Base class."""

    def test_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)


class TestBaseSaveToFile(unittest.TestCase):
    """Tests the save_to_file method of the Base class."""

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(10, 7, 2, 8, 6)
        cls.r2 = Rectangle(2, 4, 0, 0, 7)

    @classmethod
    def tearDownClass(cls):
        del cls.r1
        del cls.r2

    def test_rectangle_type(self):
        Rectangle.save_to_file([self.r1, self.r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(str, type(file.read()))

    def test_square_type(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4, 0, 0)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            self.assertEqual(str, type(file.read()))

if __name__ == "__main__":
    unittest.main()
