#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    int_sum = 0

    for i in new_list:
        int_sum += i

    return (int_sum)
