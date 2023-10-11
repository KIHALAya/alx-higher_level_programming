#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        highest_value = 0
        best_student = ""
        for i in a_dictionary:
            if a_dictionary[i] > highest_value:
                highest_value = a_dictionary[i]
                best_student = i
        return(best_student)
    else:
        return (None)
