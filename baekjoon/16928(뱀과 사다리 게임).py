from collections import deque

n, m = map(int, input().split())
data = [i for i in range(101)]
visited = [False] * 101

for i in range(n + m):
    a, b = map(int, input().split())
    data[a] = b

q = deque()
visited[1] = 0
q.append(1)
while q:
    x = q.popleft()
    for i in range(1, 7):
        nx = x + i
        if nx > 100:
            continue
        nx = data[nx]
        if not visited[nx] or visited[nx] > visited[x] + 1:
            visited[nx] = visited[x] + 1
            q.append(nx)

print(visited[100])
