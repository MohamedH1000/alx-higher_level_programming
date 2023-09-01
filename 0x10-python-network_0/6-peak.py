#!/usr/bin/python3
"""finding a peak in list of int by this script
"""

"""
    thought of processes
"""


def find_peak(list_of_integers):
    """
    force implementation for question
    """
    mx_a = None
    for a in list_of_integers:
        if mx_a is None or mx_a < a:
            mx_a = a
    return mx_a
