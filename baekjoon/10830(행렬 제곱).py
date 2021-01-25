import sys

input = sys.stdin.readline


# 행렬 곱셈
def mul(n, matrix1, matrix2):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1000

    return result


# 2분할
def devide(n, b, matrix):
    if b == 1:
        return matrix
    elif b == 2:
        return mul(n, matrix, matrix)
    else:
        tmp = devide(n, b//2, matrix)
        if b % 2 == 0:
            return mul(n, tmp, tmp)
        else:
            return mul(n, mul(n, tmp, tmp), matrix)


n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

result = devide(n, b, a)
for row in result:
    for num in row:
        print(num%1000, end = ' ')
    print()