from collections import deque
import copy
n, m = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(input().strip()))
newmap = []
for i in range(m):
    row = []
    for j in range(n):
        if graph[i][j] == "c" or graph[i][j] == ".":
            row.append(1)
        else:
            row.append(0)
    newmap.append(row)


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y,new):
    global m
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if new[nx][ny] == 0:
                continue
            if new[nx][ny] == 1:
                if i == 2 or i == 3:
                    new[nx][ny] = new[x][y] + 1
                else:
                    new[nx][ny] = new[x][y]
                q.append((nx,ny))
    return new[m-1]

minv = []
for i in range(n):
    if graph[0][i] == "c":
        new = copy.deepcopy(newmap)
        for el in bfs(0,i,new):
           if el != 0:
            minv.append(el)

if not minv:
    print(-1)
else:
    if min(minv)-1 == 0:
        print(-1)
    else:
        print(min(minv)-1)