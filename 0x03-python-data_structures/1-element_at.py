#!/usr/bin/python3
def element_at(my_list, idx):
    if my_list:
        if idx < 0 or idx >= len(my_list):
            return None
        else:
            return my_list[idx]
    else:
        return None
