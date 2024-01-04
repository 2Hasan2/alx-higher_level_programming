#!/usr/bin/python3
from calculator_1 import add, sub


def magic_calculation(a, b):

    return add(add(a, b), 9) if a < b else sub(a, b)
