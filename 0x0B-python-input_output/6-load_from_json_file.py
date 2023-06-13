#!/usr/bin/python3
"""
module that is loaded from json file
"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file
    """
    with open(filename, "r") as File:
        my_obj = json.load(File)
        return my_obj
