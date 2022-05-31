#!/usr/bin/python3
def uppercase(str):
    for x in str:
        c = x
        if(65 <= ord(c) <= 122):
            if(97 <= ord(c) <= 122):
                c = chr(ord(c) - 32)
        print(f"{c:s}", end="")
    print("")
