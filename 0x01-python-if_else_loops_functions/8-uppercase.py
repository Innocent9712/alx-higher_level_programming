#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if(65 <= ord(x) <= 122):
            if(97 <= ord(x) <= 122):
                x = chr(ord(x) - 32)
        print("{:s}".format(x), end="")
    print("")