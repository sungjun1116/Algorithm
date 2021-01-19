import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에 즉시 종료
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    # 해당 노드가 산이라면
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x - 1, y - 1)
        dfs(x - 1, y + 1)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x + 1, y - 1)
        dfs(x + 1, y + 1)
        dfs(x, y + 1)
        return True
    return False


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))

    # 모든 노드(위치)에 대해서 검
    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) is True:
                result += 1
    print(result)


