import copy
from collections import deque

r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
origin = copy.deepcopy(graph)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def clean():
    x1 = cleaner[0]
    x2 = cleaner[1]

    # 반시계방향 순환
    # 오른쪽으로 이동하는 미세먼지들
    for i in range(c):
        if i == c - 1:
            break
        if graph[x1][i] > 0:
            graph[x1][i + 1] = graph[x1][j]
            graph[x1][i] = 0

    # 위쪽으로 이동하는 미세먼지들
    for i in range(x1, -1, -1):
        if i == 0:
            break
        if graph[i][c - 1] > 0:
            graph[i - 1][c - 1] = graph[i][c - 1]
            graph[i][c - 1] = 0

    # 왼쪽으로 이동하는 미세먼지들
    for i in range(c - 1, -1, -1):
        if i == 0:
            break
        if graph[0][i] > 0:
            graph[0][i - 1] = graph[0][i]
            graph[0][i] = 0

    # 아래쪽으로 이동하는 미세먼지들
    for i in range(x1 + 1):
        if graph[i][0] > 0:
            graph[i + 1][0] = graph[i][0]
            graph[i][0] = 0
            # 공기청정기에 들어가면 정화됨
            if i + 1 == x1:
                graph[i + 1][0] = -1

    # 시계방향 순환
    # 오른쪽으로 이동하는 미세먼지들
    for i in range(c):
        if i == c - 1:
            break
        if graph[x2][j] > 0:
            graph[x2][j + 1] = graph[x2][j]
            graph[x2][j] = 0

    # 아래으로 이동하는 미세먼지들
    for i in range(x2, r):
        if i == r - 1:
            break
        if graph[i][c - 1] > 0:
            graph[i + 1][c - 1] = graph[i][c - 1]
            graph[i][c - 1] = 0

    # 왼쪽으로 이동하는 미세먼지들
    for i in range(c - 1, -1, -1):
        if i == 0:
            break
        if graph[r - 1][i] > 0:
            graph[r - 1][i - 1] = graph[r - 1][i]
            graph[r - 1][i] = 0

    # 쪽으로 이동하는 미세먼지들
    for i in range(r - 1, x2 - 1, -1):
        if graph[i][0] > 0:
            graph[i - 1][0] = graph[i][0]
            graph[i][0] = 0
            # 공기청정기에 들어가면 정화
            if i - 1 == x2:
                graph[i - 1][0] = -1


def bfs():
    time = 0
    while q:
        if time == t:
            return
        for _ in range(len(q)):
            x, y = q.popleft()
            cnt = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                if graph[nx][ny] == -1:
                    continue
                graph[nx][ny] += origin[x][y] // 5
                q.append((nx, ny))
                cnt += 1
            graph[x][y] -= (origin[x][y] // 5) * cnt

        print(graph)
        clean()
        time += 1


q = deque()
cleaner = []
for i in range(r):
    for j in range(c):
        # 미세먼지가 있는 위치
        if graph[i][j] > 0:
            q.append((i, j))
        # 공기청정기가 있는 위치
        if graph[i][j] == -1:
            cleaner.append(i)
bfs()

result = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            result += graph[i][j]
print(result)
