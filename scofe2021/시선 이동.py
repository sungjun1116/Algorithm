from collections import deque

m, n = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'x' or graph[nx][ny] == int(1e9):
                    graph[nx][ny] = int(1e9)
                    continue
                if graph[nx][ny] == 'c':
                    continue
                if visited[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
                    visited[nx][ny] = 1


for i in range(m):
    visited = [[0] * m for _ in range(n)]
    if graph[0][i] == 'c':
        graph[0][i] = 0
        bfs(0, i)
