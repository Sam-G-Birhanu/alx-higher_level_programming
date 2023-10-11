#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)

    if n == 1:
        print("0 arguments.")
    else:
        print("{:d} argument{}:".format(n - 1, "s" if n > 2 else ""))
        for idx, arg in enumerate(argv[1:], start=1):
            print("{:d}: {:}".format(idx, arg))

