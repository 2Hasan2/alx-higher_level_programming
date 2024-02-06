#!/usr/bin/python3

import os
"""Read file"""


def read_file(filename=""):
    """Read file"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
