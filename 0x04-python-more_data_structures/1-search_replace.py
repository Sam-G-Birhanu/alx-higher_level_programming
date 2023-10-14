#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for x in my_list:
        if x != search:
            new.append(x)
        else:
            x = replace
            new.append(x)
    return new
