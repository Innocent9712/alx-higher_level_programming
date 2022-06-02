#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv) - 1
    print(f"{arg_count} argument{'s' if arg_count == 0 or arg_count > 1 else ''}", end="")
    print(f"{'.' if arg_count == 0 else ':'}")
    if (arg_count > 0):
            for arg in sys.argv:
                if (sys.argv.index(arg) != 0):
                    print(f"{sys.argv.index(arg)}: {arg}")
