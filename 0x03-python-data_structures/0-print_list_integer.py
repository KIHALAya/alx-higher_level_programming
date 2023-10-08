#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        if type(i) == int:
            print("{}".format(my_list[i]))
        else:
            continue
