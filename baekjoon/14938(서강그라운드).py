INF = int(1e9)

n, m, r = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

data = list(map(int, input().split()))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    graph[b][a] = min(graph[b][a], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = -INF
for i in range(1, n + 1):
    result = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            result += data[j - 1]
    answer = max(answer, result)

print(answer)
