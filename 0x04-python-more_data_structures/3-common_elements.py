#!/usr/bin/python3
def common_elements(set_1, set_2):
    com_set = set()
    for item_1 in set_1:
        for item_2 in set_2:
            if item_1 == item_2:
                com_set.add(item_1)
    return com_set
