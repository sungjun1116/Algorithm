INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    #  성적 낮은 학생이 성적 높은 학생을 가리킴
    a, b = map(int, input().split())
    graph[a][b] = 1

# 다른 학생을 거쳐서 성적 높은 학생을 탐색할 수 있는 경우 고려
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for a in range(1, n + 1):
    count = 0
    for b in range(1, n + 1):
        # 내 처음 풀이 -> if graph[a][b] == 1 or graph[b][a] == 1:
        if graph[a][b] != INF or graph[b][a] != INF:
            count += 1
        if count == n:
            result += 1
            break

print(result)


