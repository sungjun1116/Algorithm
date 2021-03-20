rate = ['A', 'B', 'C', 'D', 'E']
data = list(map(float, input().split()))
rate = list(zip(data, rate))

n, m = map(int, input().split())
array = [list(input()) for _ in range(n)]
graph = [list(input()) for _ in range(n)]

result = []
for i in range(n):
    for j in range(m):
        if array[i][j] == 'Y':
            result.append((i, j, 2))
        if array[i][j] == 'O':
            result.append((i, j, 1))
for k in rate:
    for i in range(n):
        for j in range(m):
            if graph[i][j] == k[1]:
                graph[i][j] = (k[1], k[0])


result.sort(key=lambda x: (-x[2], -graph[x[0]][x[1]][1]))
for i in result:
    x, y = i[0], i[1]
    a, b = graph[x][y][0], graph[x][y][1]
    print(a, b, x, y)