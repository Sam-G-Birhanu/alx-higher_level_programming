#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        if idx < 0 or idx >= len(my_list):
            return my_list
        else:
            new_list = [n for n in my_list]
            new_list[idx] = element
            return new_list
    else:
        return None
