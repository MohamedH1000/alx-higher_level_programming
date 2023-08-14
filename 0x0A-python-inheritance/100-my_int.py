#!/usr/bin/python3
"""
a module that is class
"""


class MyInt(int):
    """int object in this class"""

    def __ee__(self, other):
        """method that is equal equal"""
        return super().__ee__(other)

    def __ne__(self, other):
        """a method that is not equal"""
        return super().__ne__(other)
