#!/usr/bin/python3
"""
log parsing script module
"""


import sys


if __name__ == "__main__":
    sze = [0]
    cds = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    def check_match(ln):
        '''macth in line regexp check'''
        try:
            ln = ln[:-1]
            wrds = ln.split(" ")
            sze[0] += int(wrds[-1])
            cde = int(wrds[-2])
            if cde in cds:
                cds[cde] += 1
        except ValueError:
            pass

    def print_stats():
        '''accumulated statistics to be printed'''
        print("File size: {}".format(sze[0]))
        for a in sorted(cds.keys()):
            if cds[a]:
                print("{}: {}".format(a, cds[a]))
    x = 1
    try:
        for ln in sys.stdin:
            check_match(ln)
            if x % 10 == 0:
                print_stats()
            x += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
