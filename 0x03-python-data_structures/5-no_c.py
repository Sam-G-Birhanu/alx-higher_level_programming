#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_str = ""
        for str in my_string:
            if str == 'C' or str == 'c':
                continue
            else:
                new_str = new_str + str
        return new_str
