from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    days = -1
    while q:
        days += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                    box[nx][ny] = box[x][y] + 1
                    q.append((nx, ny))

    for b in box:
        if 0 in b:
            return -1
    return days


q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))

print(bfs())

