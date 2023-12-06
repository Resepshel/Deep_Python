# Напишите функцию для транспонирования матрицы

# 1     2       3       4
# 5     6       7       8
# 9     10      11      12

# 1     5       9
# 2     6       10
# 3     7       11
# 4     8       12

def create_new_matrix(matr):
    new_matrix = [[] for _ in range(len(matr[0]))]
    for i in range(len(matr[0])):
        for j in range(len(matr)):
            new_matrix[i].append(0)
    return new_matrix


def transposition_matrix(matr):
    trans_matrix = create_new_matrix(matr)
    for i in range(len(matr)):
        for j in range(len(matr[0])):
            trans_matrix[j][i] = matr[i][j]
    return trans_matrix


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

print(transposition_matrix(matrix))


