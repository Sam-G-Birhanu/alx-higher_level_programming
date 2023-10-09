#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix and (len(matrix) != 1 and matrix[0] is not None):
        for row in matrix:
            for element in row:
                print("{:d}".format(element), end=' ')
            print()  # Move to the next line for the next row
    else:
        return None
