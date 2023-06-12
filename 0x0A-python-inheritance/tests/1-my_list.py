#!/usr/bin/python3
"""
    My list class
"""
class MyList(list):
    """class of my_list
    """

    def print_sorted(self):
        """list to be printed
        """
        print(sorted(self))
