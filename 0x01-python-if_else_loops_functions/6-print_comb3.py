#!/usr/bin/python3
for x in range(0, 10):
    for y in range(0, 10):
        if (y > x):
            if (x + y < 17):
                print("{:d}{:d}".format((x), (y)), end=", ")
            else:
                print("{:d}{:d}".format((x), (y)))
