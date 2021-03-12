from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001


def dfs(start):
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            return
        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)


dfs(n)
