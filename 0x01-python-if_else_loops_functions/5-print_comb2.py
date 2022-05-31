#!/usr/bin/python3
for x in range(0, 100):
    if (x < 99):
        print("{:d}{:d}".format((x // 10), (x % 10)), end=", ")
    else:
        print("{:d}{:d}".format((x // 10), (x % 10)))
