#!/usr/bin/python3
"""
module that append_write
"""


def append_write(filename="", text=""):
    """
    write_file - a function that append a string to a text
    """
    with open(filename, mode="a", encoding="UTF-8") as File:
        return (File.write(text))
