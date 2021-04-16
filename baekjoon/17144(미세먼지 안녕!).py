import copy
from collections import deque

r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
time = 0


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
    for i in range(1, c):
        if i == c - 1:
            break
        if graph[x2][j] > 0:
            graph[x2][j] = graph[x2][j - 1]
            graph[x2][j - 1] = 0

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
    while q:
        x, y = q.popleft()
        cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if graph[nx][ny] == -1:
                continue
            graph[nx][ny] += origin[x][y] // 5
            cnt += 1
        graph[x][y] -= (origin[x][y] // 5) * cnt


cleaner = []
for i in range(r):
    for j in range(c):
        # 공기청정기가 있는 위치
        if graph[i][j] == -1:
            cleaner.append(i)

while True:
    q = deque()
    if time == t:
        break

    for i in range(r):
        for j in range(c):
            # 미세먼지가 있는 위치
            if graph[i][j] > 0:
                q.append((i, j))

    origin = copy.deepcopy(graph)
    bfs()
    clean()
    time += 1

result = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            result += graph[i][j]
print(result)

'''
import math
from collections import deque

r, c, t = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(int, input().split())))


def pure_on(a, c):
    global graph
    temp_list = []
    for i in range(1, c):
        temp_list.append(graph[a][i])
    for i in range(a - 1, -1, -1):
        temp_list.append(graph[i][c - 1])
    for i in range(c - 2, - 1, -1):
        temp_list.append(graph[0][i])
    for i in range(1, a):
        temp_list.append(graph[i][0])

    temp_list.insert(0, 0)
    del temp_list[-1]

    q = deque(temp_list)

    for i in range(1, c):
        graph[a][i] = q.popleft()
    for i in range(a - 1, -1, -1):
        graph[i][c - 1] = q.popleft()
    for i in range(c - 2, - 1, -1):
        graph[0][i] = q.popleft()
    for i in range(1, a):
        graph[i][0] = q.popleft()


def pure_on_2(a, c):
    temp_list = []
    for i in range(1, c):
        temp_list.append(graph[a][i])

    for i in range(a + 1, r - 1):
        temp_list.append(graph[i][c - 1])
    for i in range(c - 1, - 1, -1):
        temp_list.append(graph[r - 1][i])
    for i in range(r - 2, a - 1, -1):
        temp_list.append(graph[i][0])

    temp_list.insert(0, 0)
    del temp_list[-1]

    q = deque(temp_list)

    for i in range(1, c):
        graph[a][i] = q.popleft()
    for i in range(a + 1, r - 1):
        graph[i][c - 1] = q.popleft()
    for i in range(c - 1, - 1, -1):
        graph[r - 1][i] = q.popleft()
    for i in range(r - 2, a - 1, -1):
        graph[i][0] = q.popleft()
    graph[a][0] = -1


def check(x, y):
    if 0 <= x < r and 0 <= y < c:
        if graph[x][y] != -1:
            return True
    return False


for _ in range(t):
    spd = []
    pure = []
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0 or graph[i][j] != -1:
                if graph[i][j] >= 5:
                    spd.append((i, j))
            if graph[i][j] == -1:
                pure.append([i, j])
    plus = []
    for x, y in spd:
        cnt = 0
        if check(x - 1, y):
            plus.append([x - 1, y, math.floor(graph[x][y] / 5)])
            cnt += 1
        if check(x, y - 1):
            plus.append([x, y - 1, math.floor(graph[x][y] / 5)])
            cnt += 1
        if check(x + 1, y):
            plus.append([x + 1, y, graph[x][y] // 5])
            cnt += 1
        if check(x, y + 1):
            plus.append([x, y + 1, math.floor(graph[x][y] / 5)])
            cnt += 1

        graph[x][y] = graph[x][y] - math.floor(graph[x][y] / 5) * cnt
        if graph[x][y] <= 0:
            graph[x][y] = 0

    for x, y, z in plus:
        graph[x][y] += z
    pure_cnt = 1

    for a, b in pure:

        if pure_cnt == 1:
            pure_on(a, c)
            pure_cnt += 1
        elif pure_cnt == 2:
            pure_on_2(a, c)

total = 0
for i in range(r):
    # print(graph[i])
    total += sum(graph[i])
print(total + 2)
'''
