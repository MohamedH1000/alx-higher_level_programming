#!/usr/bin/python3
"""
a module that is write file
"""


def write_file(filename="", text=""):
    """
    write_file - a string text to be write
    """
    with open(filename, mode="w", encoding="UTF-8") as File:
        return (File.write(text))
