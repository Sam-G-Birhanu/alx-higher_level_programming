#!/usr/bin/python3
def print_list_integer(my_list=[]):
    template = "{:d}"
    for n in my_list:
        num = template.format(n)
        print(num)
