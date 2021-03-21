import sys

input = sys.stdin.readline
result = 0

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def rotate(tet):
    r, c = len(tet), len(tet[0])
    return [[tet[r - 1 - j][i] for j in range(r)] for i in range(c)]


def check(tet):
    global result
    x = len(tet)
    y = len(tet[0])
    for start_x in range(n):
        if start_x + (x - 1) >= n:
            continue
        for start_y in range(m):
            temp = 0
            if start_y + (y - 1) >= m:
                continue
            for i in range(x):
                for j in range(y):
                    if tet[i][j]:
                        temp += arr[start_x + i][start_y + j]
            result = max(result, temp)


tet1 = [[1, 1, 1, 1]]
tet2 = [[1, 1], [1, 1]]
tet3 = [[1, 0], [1, 0], [1, 1]]
tet4 = [[1, 0], [1, 1], [0, 1]]
tet5 = [[1, 1, 1], [0, 1, 0]]
tet6 = [[0, 1], [1, 1], [1, 0]]
tet7 = [[0, 1], [0, 1], [1, 1]]
tet = [tet1, tet2, tet3, tet4, tet5, tet6, tet7]

for t in tet:
    for _ in range(4):
        check(t)
        t = rotate(t)

print(result)