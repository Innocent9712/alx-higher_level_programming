#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg_count = 0
    for arg in sys.argv:
        if (sys.argv.index(arg) != 0):
            arg_count += int(arg)
    print(arg_count)
                    