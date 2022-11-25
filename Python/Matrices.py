import math as math


def matrix_addition(matrixA, matrixB):

    # initialize matrix to hold the results
    matrixSum = []

    # matrix to hold a row for appending sums of each element

    # TODO: write a for loop within a for loop to iterate over
    # the matrices
    for i in range(len(matrixA)):
        row = [x + y for x, y in zip(matrixA[i], matrixB[i])]
        matrixSum.append(row)
    # TODO: As you iterate through the matrices, add matching
    # elements and append the sum to the row variable

    # TODO: When a row is filled, append the row to matrixSum.
    # Then reinitialize row as an empty list

    return matrixSum


def get_row(matrix, row):
    return matrix[row]


def get_column(matrix, column_number):
    column = []
    for i in range(len(matrix)):
        column.append(matrix[i][column_number])
    return column


def dot_product(vector_one, vector_two):
    return sum([x * y for x, y in zip(vector_one, vector_two)])


def transpose(matrix):
    matrix_transpose = []
    for i in range(len(matrix[0])):
        matrix_transpose.append(get_column(matrix, i))

    return matrix_transpose


# def matrix_multiplication(matrixA, matrixB):

#     ### TODO: store the number of rows in A and the number
#     ###       of columns in B. This will be the size of the output
#     ###       matrix
#     ### HINT: The len function in Python will be helpful
#     m_rows = len(matrixA)
#     p_columns = len(matrixB[0])

#     # empty list that will hold the product of AxB
#     result = []

#     ### TODO:  Write a for loop within a for loop. The outside
#     ###        for loop will iterate through m_rows.
#     ###        The inside for loop will iterate through p_columns.
#     for rows in range(m_rows):
#         row_result = []
#         row_list = get_row(matrixA, rows)
#         for cols in range(p_columns):
#             ### TODO:  As you iterate through the m_rows and p_columns,
#             ###        use your get_row function to grab the current A row
#             ###        and use your get_column function to grab the current
#             ###        B column.
#             col_list = get_column(matrixB, cols)

#             ### TODO: Calculate the dot product of the A row and the B column
#             product_result = dot_product(row_list, col_list)

#             ### TODO: Append the dot product to an empty list called row_result.
#             ###       This list will accumulate the values of a row
#             ###        in the result matrix
#             row_result.append(product_result)

#         ### TODO: After iterating through all of the columns in matrix B,
#         ###       append the row_result list to the result variable.
#         ###       Reinitialize the row_result to row_result = [].
#         ###       Your for loop will move down to the next row
#         ###       of matrix A.
#         ###       The loop will iterate through all of the columns
#         ###       taking the dot product
#         ###       between the row in A and each column in B.
#         result.append(row_result)
#     ### TODO: return the result of AxB

#     return result


def matrix_multiplication(matrixA, matrixB):
    product = []

    ## TODO: Take the transpose of matrixB and store the result
    ##       in a new variable
    matrixB_T = transpose(matrixB)

    ## TODO: Use a nested for loop to iterate through the rows
    ## of matrix A and the rows of the tranpose of matrix B
    for i in range(len(matrixA)):
        result = []
        ## TODO: Calculate the dot product between each row of matrix A
        ##         with each row in the transpose of matrix B
        for j in range(len(matrixB_T)):
            product_sum = sum([x * y for x, y in zip(matrixA[i], matrixB_T[j])])
            result.append(product_sum)
        ## TODO: As you calculate the results inside your for loops,
        ##       store the results in the product variable
        product.append(result)

    ## TODO:
    return product


def identity_matrix(n):

    identity = []

    # TODO: Write a nested for loop to iterate over the rows and
    # columns of the identity matrix. Remember that identity
    # matrices are square so they have the same number of rows
    # and columns
    for i in range(n):
        row = [0] * n
        row[i] = 1
        identity.append(row)

    # Make sure to assign 1 to the diagonal values and 0 everywhere
    # else

    return identity

    ##inverse in 1*1 dimension matrix[[a]] is simply muply 1/a
    ##inverse in 2*2 dimension matrix[[a,b],[c,d]] is 1/(ad-bc) * matrix[[d,-b],[-c,a]]
    ## Note that if ad = bc, then the matrix does not have inverse.


def inverse_matrix(matrix):

    inverse = []

    if len(matrix) != len(matrix[0]):
        raise ValueError("The matrix must be square")

    ## TODO: Check if matrix is larger than 2x2.
    ## If matrix is too large, then raise an error
    if len(matrix) > 2 or len(matrix[0]) > 2:
        raise ValueError("The matrix is too big")
    ## TODO: Check if matrix is 1x1 or 2x2.
    ## Depending on the matrix size, the formula for calculating
    ## the inverse is different.
    # If the matrix is 2x2, check that the matrix is invertible

    if len(matrix) == 1:
        if matrix[0] == 0:
            raise ValueError("The denominator of a fraction cannot be zero")
        inverse.append([1 / x for x in matrix[0]])
    else:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        denominator = a * d - b * c
        if denominator == 0:
            raise ValueError("The denominator of a fraction cannot be zero")

        inverse = [
            [d / denominator, -b / denominator],
            [-c / denominator, a / denominator],
        ]

    ## TODO: Calculate the inverse of the square 1x1 or 2x2 matrix.

    return inverse
