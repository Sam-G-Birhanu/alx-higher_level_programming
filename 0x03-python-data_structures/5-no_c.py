#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_str = ""
        for char in my_string:
            if char == 'C' or char == 'c':
                continue
            else:
                new_str = new_str + char
        return new_str
