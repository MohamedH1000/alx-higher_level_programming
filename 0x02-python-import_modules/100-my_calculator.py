#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    argv = sys.argv[1:]
    na = len(argv)
    if na != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    elif sys.argv[2] not in '+-*/':
        print('Unknown operator. Available operators: +, -, *, and /')
        exit(1)
    else:
        x = int(sys.argv[1])
        y = int(sys.argv[3])
        if sys.argv[2] == '+':
            print('{:d} + {:d} = {:d}'.format(x, y, add(x, y)))
        elif sys.argv[2] == '-':
            print('{:d} - {:d} = {:d}'.format(x, y, sub(x, y)))
        elif sys.argv[2] == '*':
            print('{:d} * {:d} = {:d}'.format(x, y, mul(x, y)))
        elif sys.argv[2] == "/":
            print('{:d} / {:d} = {:d}'.format(x, y, div(x, y)))
