#!/usr/bin/python3


"""Save to JSON file"""


import json


def save_to_json_file(my_obj, filename):
    """Save to JSON file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(json.dumps(my_obj))
