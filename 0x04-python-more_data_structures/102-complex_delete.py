#!/usr/bin/python3
def complex_delete(my_dict, value):
    copy = my_dict.copy()
    for i, j in copy.items():
        if value in j:
            del my_dict[i]
    return my_dict
