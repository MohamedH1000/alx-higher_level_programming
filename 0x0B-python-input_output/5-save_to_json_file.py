#!/usr/bin/python3
"""
json module to save
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file
    """
    with open(filename, "w") as File:
        json.dump(my_obj, File)
