#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_args = len(argv)
    total = 0
    for i in range(1, num_args):
        total += i
    print("{:d} arguments: ".format(total))
    for idx in range(1, num_args):
        print("{:d} : {:} ".format(idx, argv[idx]))
