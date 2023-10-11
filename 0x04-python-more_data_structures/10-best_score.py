#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        keys = list(a_dictionary.keys())
        highest = 0
        best = ""
        for i in keys:
            if a_dictionary[i] > highest:
                highest = a_dictionary[i]
                best = i
        return (best)
