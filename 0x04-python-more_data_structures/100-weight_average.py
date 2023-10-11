#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        mul = 1
        w_sm = 0
        sm = 0
        average = 0
        for i in my_list:
            sm += i[0] * i[1]
            w_sm += i[1]

        average = sm / w_sm
        return (average)
