#!/usr/bin/python3
"""Defines a matrix division function."""

def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if matrix:
        leng = len(matrix[0])
        c1 = 0
        c2 = 0
        f_matrix = []
        for i in matrix:
            new_matrix = []
            for j in i:
                # print(j)
                if not isinstance(j, (int,float)):
                    my_err = "matrix must be a matrix (list of lists) of integers/floats"
                    raise TypeError(my_err)
                if len(matrix[0]) != leng:
                    my_err = "Each row of the matrix must have the same size"
                    raise TypeError(my_err)
                if not isinstance(div, (int,float)):
                    raise TypeError("div must be a number")
                if div == 0:
                    raise ZeroDivisionError("division by zero")
                new_matrix.append(round((j / div), 2))
            f_matrix.append(new_matrix)
    return f_matrix
                
