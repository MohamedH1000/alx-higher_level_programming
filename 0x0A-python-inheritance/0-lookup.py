#!/usr/bin/python3
"""
lookup to the attribute
"""


def lookup(obj):
    """ calss looking an attribute
    Args:
        obj: class object
    Returns:
        Nothing
    """
    return [a for a in dir(obj)]
