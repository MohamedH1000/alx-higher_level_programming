#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    an = len(argv)
    a = 1
    if an == 0:
        print("{:d} arguments.".format(an))
    elif an == 1:
        print("{:d} argument.".format(an))
        print("{:d}: {:s}".format(a, sys.argv[1]))
    else:
        print("{:d} arguments.".format(an))
        while a <= an:
            print("{:d}: {:s}".format(a, sys.argv[a]))
            a += 1
