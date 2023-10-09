#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        template = "{:d}"
        idx = len(my_list) - 1
        for n in range(len(my_list)):
            n = my_list[idx]
            num = template.format(n)
            print(num)
            idx -= 1
