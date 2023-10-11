#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temp = a_dictionary.copy()
    for i in temp:
        if temp[i] == value:
            del a_dictionary[i]

    return (a_dictionary)
