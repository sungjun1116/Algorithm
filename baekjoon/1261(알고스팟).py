'''
[0-1 너비 우선 탐색]
최소 거리를 구하는 문제이기 때문에 BFS를 이용한다.
각 방을 노드로, 방과 방 사이를 이동하는데 부숴야하는 벽의 수를 노드 간 이동 비용이라고 했을 때,
벽이 없는 방(0)으로 이동하는데에는 비용이 0, 부숴야 하는 벽(1)으로 이동하는데에는 비용이 1 소모되는
0과 1의 비용을 가진 탐색이 된다.
'''

import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())
a = [list(input()) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    dist[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny] == -1:
                    # 갈 수 있는 노드에 대한 비용이 0이면 앞에 추가(같은 레벨의 정점 삽입)
                    if a[nx][ny] == '0':
                        q.appendleft([nx, ny])
                        dist[nx][ny] = dist[x][y]
                    # 갈 수 있는 노드에 대한 비용이 1이면 에 추가(다른 레벨의 정점 삽입)
                    elif a[nx][ny] == '1':
                        q.append([nx, ny])
                        dist[nx][ny] = dist[x][y] + 1


bfs(0,0)

'''
비용이 적은 경로부터 우선적으로 탐색하고, 
가장 적은 비용에 대한 탐색이 끝나고 나서야 비로소 더 큰 비용의 경로를 탐색하기 시작하기 때문에 
벽을 최소한으로 부수고 이동하는 경로를 찾을 수있게 된다.
'''

print(dist[n - 1][m - 1])
