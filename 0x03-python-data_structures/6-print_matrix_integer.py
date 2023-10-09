#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix and (len(matrix) != 1 and matrix[0] is not None):
        template = "{:d} {:d} {:d}"
        for i in matrix:
            new_mat = []
            for j in i:
                new_mat.append(j)
            num = template.format(*new_mat)
            print(num)
    else:
        return None
