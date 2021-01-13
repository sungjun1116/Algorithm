from collections import deque
INF = 1e9

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


now_size = 2
now_x = 0
now_y = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            now_x, now_y = i, j
            graph[now_x][now_y] = 0

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 최단거리 테이블을 만들기 위핸 bfs 함수
def bfs():
    dist = [[-1] * n for _ in range(n)]
    q = deque([])
    while q:
        x, y = q.popleft([(now_x, now_y)])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 자신의 크기보다 작거나 같은 경우에 지나갈 수 있음
                if dist[nx][ny] == -1 and graph[nx][ny] <= now_size:
                    dist[nx][ny] = dist[nx][ny] + 1
                    q.append((nx, ny))
    return dist


# 최단 거리 테이블이 주어졌을 때, 먹을 물고기를 찾는 함수
def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            # 도달이 가능하면서 먹을 수 있는 물고기일 때
            if dist[i][j] != -1 and dist[i][j] < min_dist and 1 <= graph[i][j] < now_size:
                x, y = i, j
                min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist


result = 0
ate = 0  # 현재 크기에서 먹은 양
while True:
    # 먹을 수 있는 물고기의 위치 찾기
    value = find(bfs())
    if value is None:
        print(result)
        break
    else:
        # 현재 위치 갱신 및 이동 거리 변경
        now_x, now_y = value[0], value[1]
        result += value[2]
        # 먹은 위치에는 이제 아무것도 없도록 처리
        graph[now_x][now_y] = 0
        ate += 1
        if ate >= now_size:
            now_size += 1
            ate = 0
