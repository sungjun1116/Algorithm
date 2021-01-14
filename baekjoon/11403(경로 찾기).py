INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정


n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = INF

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(n):
    for b in range(n):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] != INF:
            print(1, end=" ")
        else: print(0, end=" ")
    print()



