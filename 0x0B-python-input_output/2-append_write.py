#!/usr/bin/python3

"""Append to a file"""


def append_write(filename="", text=""):
    """Append to a file"""
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
