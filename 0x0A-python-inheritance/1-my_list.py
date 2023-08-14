#!/usr/bin/python3
"""
    my list contained in a class
"""


class MyList(list):
    """class of my_list
    """

    def print_sorted(self):
        """list to be printed
        """
        print(sorted(self))
