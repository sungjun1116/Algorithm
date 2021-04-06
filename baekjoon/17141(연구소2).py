import copy
import itertools
import sys
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def max_arr(array, virus):
    ans = -INF
    for i in range(n):
        for j in range(n):
            if array[i][j] == 0 and (i, j) not in virus:
                return INF
            if isinstance(array[i][j], str):
                continue
            ans = max(ans, array[i][j])
    return ans


def bfs():
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if visited[nx][ny] == 1:
                    continue

                if array[nx][ny] != '-':
                    visited[nx][ny] = 1
                    array[nx][ny] = array[x][y] + 1
                    q.append((nx, ny))


data = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            data.append((i, j))

viruses = []
for x in itertools.combinations(data, m):
    x = list(x)
    viruses.append(x)

result = INF
for virus in viruses:
    q = deque()
    visited = [[0] * n for _ in range(n)]
    array = copy.deepcopy(arr)

    for v in virus:
        q.append(v)
        visited[v[0]][v[1]] = 1
        array[v[0]][v[1]] = 0

    for i in range(n):
        for j in range(n):
            if array[i][j] == 1:
                array[i][j] = '-'

    bfs()
    temp = max_arr(array, virus)
    result = min(result, temp)

if result == INF:
    print(-1)
else:
    print(result)