#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    temp_list = []

    for i in matrix:
        for j in i:
            temp_list.append(j * j)

        square_matrix.append(temp_list)
        temp_list = []

    return (square_matrix)
