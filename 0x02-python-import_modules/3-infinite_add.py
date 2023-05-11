#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    noa = len(argv) - 1
    if noa == 0:
        print("{}".format(noa))
    else:
        res = []
        for a in range(1, noa + 1):
            res.append(int(argv[a]))
        print("{}".format(sum(res)))
