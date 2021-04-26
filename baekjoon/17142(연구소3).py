from itertools import combinations
from collections import deque
from sys import stdin

n, m = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
input = stdin.readline

arr = []
viruses = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 2:
            viruses.append((i, j, 0))
    arr.append(temp)


def check(array):
    for i in range(n):
        for j in range(n):
            if array[i][j] == 0:
                return -1
    return 0


def bfs(start, array):
    visited = [[0] * n for _ in range(n)]
    array = [a[:] for a in array]
    q = deque(start)

    # 0이 2로바뀌는 마지막 순간만 확인하면 된다.
    last = 0
    while q:
        x, y, cnt = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and array[nx][ny] != 1:
                visited[nx][ny] = 1
                if array[nx][ny] == 0:
                    array[nx][ny] = 2
                    last = cnt + 1
                q.append((nx, ny, cnt + 1))

    if check(array) == 0:
        return last
    else:
        return -1


answer = int(1e9)
for value in combinations(viruses, m):
    result = bfs(list(value), arr)
    if 0 <= result < answer:
        answer = result

print(-1 if answer == int(1e9) else answer)