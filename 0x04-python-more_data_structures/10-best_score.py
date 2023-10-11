#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        values = []
        for i in a_dictionary:
            values.append(a_dictionary[i])
        values.sort()
        values.reverse()
        best = values[0]
        for student in a_dictionary:
            if a_dictionary[student] == best:
                return(student)
    else:
        return (None)
