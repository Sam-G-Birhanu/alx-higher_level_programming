def matrix_divided(matrix, div):
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
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                if len(matrix[0]) != leng:
                    raise TypeError("Each row of the matrix must have the same size")
                if not isinstance(div, (int,float)):
                    raise TypeError("div must be a number")
                if div == 0:
                    raise ZeroDivisionError("division by zero")
                new_matrix.append(round((j / div), 2))
            f_matrix.append(new_matrix)
    return f_matrix
                
