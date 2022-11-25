import math as math
import Matrices

assert Matrices.matrix_addition([[1, 2, 3]], [[4, 5, 6]]) == [[5, 7, 9]]

assert Matrices.matrix_addition([[4]], [[5]]) == [[9]]

assert Matrices.matrix_addition([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]) == [
    [8, 10, 12],
    [14, 16, 18],
]

assert Matrices.get_column([[1, 2, 4], [7, 8, 1], [5, 2, 1]], 1) == [2, 8, 2]

assert Matrices.get_column([[5]], 0) == [5]

assert Matrices.dot_product([4, 5, 1], [2, 1, 5]) == 18
assert Matrices.dot_product([6], [7]) == 42

assert Matrices.matrix_multiplication([[5], [2]], [[5, 1]]) == [[25, 5], [10, 2]]
assert Matrices.matrix_multiplication([[5, 1]], [[5], [2]]) == [[27]]
assert Matrices.matrix_multiplication([[4]], [[3]]) == [[12]]
assert Matrices.matrix_multiplication(
    [[2, 1, 8, 2, 1], [5, 6, 4, 2, 1]],
    [[1, 7, 2], [2, 6, 3], [3, 1, 1], [1, 20, 1], [7, 4, 16]],
) == [[37, 72, 33], [38, 119, 50]]

assert Matrices.transpose([[5, 4, 1, 7], [2, 1, 3, 5]]) == [
    [5, 2],
    [4, 1],
    [1, 3],
    [7, 5],
]
assert Matrices.transpose([[5]]) == [[5]]
assert Matrices.transpose([[5, 3, 2], [7, 1, 4], [1, 1, 2], [8, 9, 1]]) == [
    [5, 7, 1, 8],
    [3, 1, 1, 9],
    [2, 4, 2, 1],
]


assert Matrices.matrix_multiplication(
    [[5, 3, 1], [6, 2, 7]], [[4, 2], [8, 1], [7, 4]]
) == [[51, 17], [89, 42]]

assert Matrices.matrix_multiplication([[5]], [[4]]) == [[20]]

assert Matrices.matrix_multiplication(
    [[2, 8, 1, 2, 9], [7, 9, 1, 10, 5], [8, 4, 11, 98, 2], [5, 5, 4, 4, 1]],
    [[4], [2], [17], [80], [2]],
) == [[219], [873], [8071], [420]]


assert Matrices.matrix_multiplication(
    [[2, 8, 1, 2, 9], [7, 9, 1, 10, 5], [8, 4, 11, 98, 2], [5, 5, 4, 4, 1]],
    [[4, 1, 2], [2, 3, 1], [17, 8, 1], [1, 3, 0], [2, 1, 4]],
) == [[61, 49, 49], [83, 77, 44], [329, 404, 39], [104, 65, 23]]

assert Matrices.identity_matrix(1) == [[1]]

assert Matrices.identity_matrix(2) == [[1, 0], [0, 1]]

assert Matrices.identity_matrix(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

assert Matrices.identity_matrix(4) == [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]
m = [[5, 9, 2, 4], [3, 8, 5, 6], [1, 0, 0, 15]]

assert Matrices.matrix_multiplication(m, Matrices.identity_matrix(4)) == m
assert Matrices.matrix_multiplication(Matrices.identity_matrix(3), m) == m

assert Matrices.inverse_matrix([[100]]) == [[0.01]]
assert Matrices.inverse_matrix([[4, 5], [7, 1]]) == [
    [-0.03225806451612903, 0.16129032258064516],
    [0.22580645161290322, -0.12903225806451613],
]

Matrices.inverse_matrix([[4, 2], [14, 7]])

Matrices.inverse_matrix([[4, 5, 1], [2, 9, 7], [6, 3, 9]])
