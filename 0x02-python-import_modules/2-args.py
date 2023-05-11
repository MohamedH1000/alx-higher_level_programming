#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    arg_num = len(argv)
    a = 1
    if arg_num == 0:
        print("{:d} arguments.".format(arg_num))
    elif arg_num == 1:
        print("{:d} argument.".format(arg_num))
        print("{:d}: {:s}".format(a, sys.argv[1]))
    else:
        print("{:d} arguments.".format(arg_num))
        while a < arg_num:
            print("{:d}: {:s}".format(a, sys.argv[a]))
            a += 1
