#!/usr/bin/python3
"""
a module method
"""


def add_attribute(ob, obnm, val):
    """ attribute to object to be added
    """
    if hasattr(ob, "__dict__") == False:
        raise TypeError("can't add new attribute")
    setattr(ob, obnm, val)
