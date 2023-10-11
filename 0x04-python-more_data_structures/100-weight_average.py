#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sm = 0
        hsm = 0

        for each in my_list:
            sm += each[0] * each[1]
            hsm += each[1]

        return (sm / hsm)
