#!/usr/bin/python3

"""Append after"""


def append_after(filename="", search_string="", new_string=""):
    """Append after"""
    with open(filename, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if search_string in lines[i]:
                lines.insert(i + 1, new_string)
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write("".join(lines))
