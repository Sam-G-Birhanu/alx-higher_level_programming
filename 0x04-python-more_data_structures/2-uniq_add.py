#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    total = 0
    for x in my_list:
        if x not in new:
            new.append(x)
    for num in new:
        total += num
    return total
