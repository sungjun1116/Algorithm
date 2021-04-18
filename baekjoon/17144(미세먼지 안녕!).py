from collections import deque
import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
time = 0


def clean():
    x1 = cleaner[0]
    x2 = cleaner[1]

    # 반시계방향 순환
    temp = deque()
    # 오른쪽으로 이동하는 미세먼지들
    for i in range(1, c):
        temp.append(graph[x1][i])

    # 위쪽으로 이동하는 미세먼지들
    for i in range(x1 - 1, -1, -1):
        temp.append(graph[i][c - 1])

    # 왼쪽으로 이동하는 미세먼지들
    for i in range(c - 2, -1, -1):
        temp.append(graph[0][i])

    # 아래쪽으로 이동하는 미세먼지들
    for i in range(1, x1):
        temp.append(graph[i][0])

    temp.appendleft(0)
    temp.pop()

    for i in range(1, c):
        graph[x1][i] = temp.popleft()

    for i in range(x1 - 1, -1, -1):
        graph[i][c - 1] = temp.popleft()

    for i in range(c - 2, -1, -1):
        graph[0][i] = temp.popleft()

    for i in range(1, x1):
        graph[i][0] = temp.popleft()

    # 시계방향 순환
    # 오른쪽으로 이동하는 미세먼지들
    for i in range(1, c):
        temp.append(graph[x2][i])

    # 아래으로 이동하는 미세먼지들
    for i in range(x2 + 1, r):
        temp.append(graph[i][c - 1])

    # 왼쪽으로 이동하는 미세먼지들
    for i in range(c - 2, -1, -1):
        temp.append(graph[r - 1][i])

    # 위쪽으로 이동하는 미세먼지들
    for i in range(r - 2, x2, -1):
        temp.append(graph[i][0])

    temp.appendleft(0)
    temp.pop()

    for i in range(1, c):
        graph[x2][i] = temp.popleft()

    for i in range(x2 + 1, r):
        graph[i][c - 1] = temp.popleft()

    for i in range(c - 2, -1, -1):
        graph[r - 1][i] = temp.popleft()

    for i in range(r - 2, x2, -1):
        graph[i][0] = temp.popleft()


def bfs():
    while q:
        x, y, value = q.popleft()
        cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if graph[nx][ny] == -1:
                continue
            graph[nx][ny] += value // 5
            cnt += 1
        graph[x][y] -= value // 5 * cnt


cleaner = []
for i in range(r):
    if graph[i][0] == -1:
        cleaner.append(i)

for _ in range(t):
    q = deque()
    for i in range(r):
        for j in range(c):
            # 미세먼지가 있는 위치
            if graph[i][j] > 0:
                q.append((i, j, graph[i][j]))  # 이 기법이 핵심
    bfs()
    clean()

result = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            result += graph[i][j]
print(result)
