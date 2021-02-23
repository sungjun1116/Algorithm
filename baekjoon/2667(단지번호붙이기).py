n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, num):
    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1:
                num = dfs(nx, ny, num + 1)
    return num


answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer.append(dfs(i, j, 1))

print(len(answer))
for i in sorted(answer):
    print(i)
