#!/usr/bin/python3
def best_score(a_dictionary):
    max_num = 0
    f_val = ""
    if a_dictionary is None:
        print("Best score: {}".format(None))
        return None
    else:
        for val, num in a_dictionary.items():
            if num > max_num:
                max_num = num
                f_val = val
    print("Best score: {}".format(f_val))
    return f_val
