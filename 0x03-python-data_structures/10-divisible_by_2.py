#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mult_list = []
    if my_list:
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                mult_list.append(True)
            else:
                mult_list.append(False)

    return (mult_list)
