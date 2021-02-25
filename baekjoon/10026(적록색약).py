import sys
import copy

sys.setrecursionlimit(10 ** 6)

n = int(input())


graph = [list(input()) for _ in range(n)]
graph2 = copy.deepcopy(graph)  # 적록색약용 리스트
for i in range(n):
    for j in range(n):
        if graph2[i][j] == 'G':
            graph2[i][j] = 'R'


def dfs(array, x, y, color):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    array[x][y] = -1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] is False:
            if array[nx][ny] == color:
                dfs(array, nx, ny, color)
                visited[nx][ny] = True


colors = ['R', 'G', 'B']
normal = [0, 0, 0]
color_weakness = [0, 0, 0]

# 적록색약이 아닌 사람이 봤을때
visited = [[False for _ in range(n)] for _ in range(n)]
for c in range(len(colors)):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == colors[c]:
                dfs(graph, i, j, colors[c])
                normal[c] += 1

# 적록색약인 사람이 봤을때
visited = [[False for _ in range(n)] for _ in range(n)]
for c in range(len(colors)):
    for i in range(n):
        for j in range(n):
            if graph2[i][j] == colors[c]:
                dfs(graph2, i, j, colors[c])
                color_weakness[c] += 1

print(sum(normal), sum(color_weakness))
