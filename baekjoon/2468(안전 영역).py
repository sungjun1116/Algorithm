import copy
import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]


def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    arr[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] is False:
            if arr[nx][ny] == 1:
                dfs(nx, ny)
                visited[nx][ny] = True


height = 1
result = []
while True:
    arr = copy.deepcopy(array)
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] < height:
                arr[i][j] = 0
            else:
                arr[i][j] = 1
    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                dfs(i, j)
                count += 1

    result.append(count)

    if count == 0:
        break

    height += 1

print(max(result))