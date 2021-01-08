from collections import *

n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 입력으로 주어지는 간선이 양방향이기 때문에 추가

# 정점 번호가 작은 것을 먼저 방문하도록 하기 위해 오름차순 정렬
for i in range(n + 1):
    graph[i].sort()


def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = False
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if visited[i]:
                queue.append(i)
                visited[i] = False

visited = [False] * (n + 1)

dfs(graph, start, visited)
print()
bfs(graph, start, visited)


