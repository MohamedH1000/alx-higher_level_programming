#!/usr/bin/python3
"""
method append after method module
"""


def append_after(filename="", search_string="", new_string=""):
    '''inser string and append method'''
    lins = []
    with open(filename, "r", encoding="utf-8") as File:
        lins = File.readlines()
        a = 0
        while a < len(lins):
            if search_string in lins[a]:
                lins[a:a + 1] = [lins[a], new_string]
                a += 1
            a += 1
    with open(filename, "w", encoding="utf-8") as File:
        File.writelines(lins)
