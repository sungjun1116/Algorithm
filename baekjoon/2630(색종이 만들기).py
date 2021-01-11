n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

white = 0
blue = 0


def quadtree(x, y, n):
    global white, blue
    check = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != graph[i][j]:  # 같은 색이 아닌 구역을 만날 경우
                quadtree(x, y, n//2)
                quadtree(x, y + n//2, n//2)
                quadtree(x + n//2, y, n//2)
                quadtree(x + n//2, y + n//2, n//2)
                return

    # 모두 white
    if check == 0:
        white += 1
        return
    # 모두 blue
    else:
        blue += 1
        return


quadtree(0, 0, n)
print(white)
print(blue)








