from collections import *

n, k = map(int, input().split())

graph = []
data = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

# 낮은 번호의 바이러스가 먼저 증식하므로 오름차순 정렬
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져 나갈 수 있는 4가지 위치
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])