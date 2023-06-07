#!/usr/bin/python3
""" a function that prints a string with certain cases """


def text_indentation(text):
    """ to print a special character cases like '.', '?', ':'
        and when this is encountered print double \n
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for a in ".:?":
        text = (a + "\n\n").join([b.strip(" ") for b in text.split(a)])
    print(text, end="")
