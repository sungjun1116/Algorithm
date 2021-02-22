from collections import deque

n = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]
info = deque()

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 동, 북, 서,
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 1, 1
data[x][y] = 2
time = 0
direction = 0
q = deque([(x, y)])
while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
        if data[nx][ny] == 0:
            data[nx][ny] = 2
            q.append((nx, ny))
            px, py = q.popleft()
            data[px][py] = 0
        else:
            data[nx][ny] = 2
            q.append((nx, ny))
    else:
        time += 1
        break
    x, y = nx, ny
    time += 1

    if info and time == info[0][0]:
        if info[0][1] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        info.popleft()

print(time)