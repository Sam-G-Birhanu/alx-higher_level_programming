#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ord_lst = sorted(a_dictionary)
    for key in ord_lst:
        print("{} : {}".format(key, a_dictionary[key]))
