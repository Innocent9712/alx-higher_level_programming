#!/usr/bin/python3
import sys

from inspect import Arguments


def safe_print_integer_err(value):
    val_is_integer = True
    try:
        print("{:d}".format(value))
    except Exception as exc:
        print("Exception: {:s}".format(exc.args[0]), file=sys.stderr)
        val_is_integer = False
    return val_is_integer
