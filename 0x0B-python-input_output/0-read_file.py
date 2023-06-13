#!/usr/bin/python3
def read_file(filename=""):
    """to print out to stdout and read the text file by this function"""

    with open(filename, encoding='utf-8') as File:
        print(File.read(), end="")
