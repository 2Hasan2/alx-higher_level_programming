#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as err:
        result = None
        sys.stderr.write("Exception: {}\n".format(err))
    return result
