#!/usr/bin/python3
"""
the module method
"""


def inherits_from(obj, a_class):
    """ to check the instance of the class in object
    """

    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
