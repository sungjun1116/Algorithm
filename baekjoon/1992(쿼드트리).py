n = int(input())
graph = []
for i in range(n):
    graph.append(list(input()))


def quadtree(x, y, n):
    check = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != graph[i][j]:  # 같은 색이 아닌 구역을 만날 경우
                a = quadtree(x, y, n//2)
                b = quadtree(x, y + n//2, n//2)
                c = quadtree(x + n//2, y, n//2)
                d = quadtree(x + n//2, y + n//2, n//2)
                return "(" + a + b + c + d + ")"

    # 모두 0
    if check == "0":
        return "0"
    # 모두 1
    else:
        return "1"


print(quadtree(0, 0, n))









