def rotate_a_matrix_by_90_degree(arr):
    return list(zip(*arr[::-1]))


a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]
print(rotate_a_matrix_by_90_degree(a))
