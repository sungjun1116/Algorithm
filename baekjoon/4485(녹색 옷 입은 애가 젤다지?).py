import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dijkstra(start):
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0
    while q:
        dist, x, y = heapq.heappop(q)
        if x == n - 1 and y == n - 1:
            print("Problem {0}: {1}".format(cnt, dist))
            return
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))


cnt = 1
while True:
    n = int(input())
    if n == 0:
        break

    graph = [list(map(int, input().split())) for i in range(n)]
    distance = [[INF] * (n + 1) for _ in range(n)]
    dijkstra(cnt)
    cnt += 1


