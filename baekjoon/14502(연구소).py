import itertools
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if lab[nx][ny] == 0:
                lab[nx][ny] = 2
                bfs(nx, ny)


def block(array, wall):
    for item in wall:
        x = item[0]
        y = item[1]
        array[x][y] = 1
    return array


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

data = [i for i in range(n*m)]
walls = []
for x in itertools.combinations(data, 3):
    x = list(x)
    for i in range(len(x)):
        if x[i] < m:
            x[i] = (0, x[i])
        else:
            x[i] = (x[i] // m, x[i] % m)
    cnt = 0
    for i in range(len(x)):
        if arr[x[i][0]][x[i][1]] != 0:
            continue
        else:
            cnt += 1
    if cnt == 3:
        walls.append(x)

result = 0
for wall in walls:
    temp = copy.deepcopy(arr)
    lab = block(temp, wall)
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                bfs(i, j)

    cnt2 = 0
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                cnt2 += 1
    result = max(result, cnt2)


print(result)

