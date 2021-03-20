from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

result = []
cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt += 1
result.append(cnt)
print(result)
