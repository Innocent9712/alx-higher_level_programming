#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    arg_count = len(sys.argv)
    if (arg_count != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    symbol = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if (symbol == '+'):
        print("{} + {} = {}".format(a, b, add(a, b)))
        exit(0)
    elif (symbol == '-'):
        print("{} - {} = {}".format(a, b, sub(a, b)))
        exit(0)
    elif (symbol == '*'):
        print("{} * {} = {}".format(a, b, mul(a, b)))
        exit(0)
    elif (symbol == '/'):
        print("{} / {} = {}".format(a, b, div(a, b)))
        exit(0)
    else:
        print("Available operators: +, -, * and /")
        exit(1)
