#!/usr/bin/python3
for a in range(0, 10):
    for b in range(1, 10):
        if a >= b:
            continue
        if a == 8 and b == 9:
            print("{:d}{:d}".format(a, b))
        else:
            print("{:d}{:d}".format(a, b), end=", ")
