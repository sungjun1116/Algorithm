from itertools import combinations
from collections import deque
from sys import stdin

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
input = stdin.readline


def block(array):
    for i in range(n):
        for j in range(n):
            if array[i][j] == 1:
                array[i][j] = -1


def bfs(array):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if array[nx][ny] == -1:
                continue
            if not visited[nx][ny]:
                array[nx][ny] = array[x][y] + 1
                visited[nx][ny] = True
                q.append((nx, ny))


def time(array):
    answer = 0
    flag = True
    for i in range(n):
        for j in range(n):
            if array[i][j] == -1:
                continue
            if (i, j) not in viruses:
                if array[i][j] == 0:
                    return -1
                answer = max(answer, array[i][j])
                flag = False

    if flag:
        return 0
    else:
        return answer


# 바이러스의 위치 담기
viruses = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            viruses.append((i, j))

result = []
for x in combinations(viruses, m):
    x = list(x)
    q = deque(x)
    graph = [item[:] for item in arr]
    visited = [[False] * n for _ in range(n)]
    for virus in x:
        a, b = virus[0], virus[1]
        graph[a][b] = 0
        visited[a][b] = True

    block(graph)
    bfs(graph)
    result.append(time(graph))

if result.count(-1) == len(result):
    print(-1)
else:
    result = list(filter(lambda item: item >= 0, result))
    print(min(result))
