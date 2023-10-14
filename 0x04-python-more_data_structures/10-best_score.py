#!/usr/bin/python3
def best_score(a_dictionary):
    max_num = 0
    f_val = ""
    if a_dictionary:
        for val, num in a_dictionary.items():
            if num > max_num:
                max_num = num
                f_val = val
    else:
        f_val = None
    return f_val
