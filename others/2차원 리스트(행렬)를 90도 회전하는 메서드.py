def rotate_a_matrix_by_90_degree(paper):
    r, c = len(paper), len(paper[0])
    return [[paper[r - 1 - j][i] for j in range(r)] for i in range(c)]


a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]
print(rotate_a_matrix_by_90_degree(a))
