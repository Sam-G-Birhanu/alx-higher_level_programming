#!/usr/bin/python3
def add(a, b):
    sum_result = a + b
    return sum_result

if __name__ == "__main__":
    import sys
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])
    result = add(arg1, arg2)
    print("{:d}".format(result))
