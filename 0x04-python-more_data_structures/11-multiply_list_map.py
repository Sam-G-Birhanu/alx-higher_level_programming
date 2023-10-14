#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    def smallf(num):
        return (num * number)
    mul = map(smallf, my_list)
    new = list(mul)
    return new
