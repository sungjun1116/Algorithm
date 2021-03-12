from collections import deque

n, m = map(int, input().split())
array = [list(input()) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[0] * m for _ in range(n)]


def bfs():
    # 불 퍼트리기
    length_fq = len(fq)
    while length_fq:
        x, y = fq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if array[nx][ny] == '.':
                    array[nx][ny] = 'F'
                    fq.append((nx, ny))
        length_fq -= 1

    # 지훈이 이동하기
    length_q = len(q)
    while length_q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                print(visited[x][y])
                return
            else:
                if array[nx][ny] == '.' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])
        length_q -= 1

    if q:
        bfs()
    else:
        print("IMPOSSIBLE")


q, fq = deque(), deque()
for i in range(n):
    for j in range(m):
        if array[i][j] == 'J':
            q.append([i, j])
            visited[i][j] = 1
            array[i][j] = '.'
        elif array[i][j] == 'F':
            visited[i][j] = 1
            fq.append([i, j])

bfs()
