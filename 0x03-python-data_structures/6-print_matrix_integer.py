#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if type(matrix) == list:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print("{:d}{}".format(matrix[i][j],
                      '' if j == len(matrix[i]) - 1 else ' '), end="")
            print("$")
    else:
        print(matrix, end="")
        print("$")
