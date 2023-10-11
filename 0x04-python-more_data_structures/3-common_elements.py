#!/usr/bin/python3
def common_elements(set_1, set_2):
    com_set = set()
    for i in set_1:
        for j in set_2:
            if i == j:
                com_set.add(i)
    return (com_set)
