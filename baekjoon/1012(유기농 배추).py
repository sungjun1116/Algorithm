import sys
sys.setrecursionlimit(10 ** 6)


def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                dfs(nx, ny)


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)
