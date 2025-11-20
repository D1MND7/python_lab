# 1
def transpose(matrix):
    if not matrix:
        return []

    for el_mat in matrix:
        if len(el_mat) != len(matrix[0]):
            raise ValueError

    result = []
    for i in range(len(matrix[0])):
        transposes = []
        for j in range(len(matrix)):
            transposes.append(matrix[j][i])
        result.append(transposes)
    return result


print("transpose")
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))


# 2
def row_sums(sum_matrix):
    if not sum_matrix:
        return []

    for el_mat in sum_matrix:
        if len(el_mat) != len(sum_matrix[0]):
            raise ValueError

    summa = []
    for el_mat in sum_matrix:
        el_sum = sum(el_mat)
        summa.append(el_sum)
    return summa


print("row_sums")
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))


# 3
def col_sums(col_matrix):
    if not col_matrix:
        return []

    for el_mat in col_matrix:
        if len(el_mat) != len(col_matrix[0]):
            raise ValueError
    result = []
    for i in range(len(col_matrix[0])):
        summ = 0
        for j in range(len(col_matrix)):
            summ += col_matrix[j][i]
        result.append(summ)
    return result


print("col_sums")
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
