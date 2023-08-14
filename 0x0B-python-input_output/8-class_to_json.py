#!/usr/bin/python3
"""
json module for class
"""


def class_to_json(obj):
    """
        simple data structure that return dictionary representation
    """
    return obj.__dict__
