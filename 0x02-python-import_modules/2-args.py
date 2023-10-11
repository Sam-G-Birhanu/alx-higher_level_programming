#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_args = len(argv)

    if num_args == 1:
        print("0 arguments.")
    else:
        print("{:d} argument{}:".format(num_args - 1, "s" if num_args > 2 else ""))
        for idx, arg in enumerate(argv[1:], start=1):
            print("{:d}: {:}".format(idx, arg))

