from collections import deque
import sys

input = sys.stdin.readline


# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue)구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = 0
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[v] + 1


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [-1] * (n + 1)

# 정의된 BFS 함수 호출
bfs(graph, x, visited)

flag = False
for i in range(1, n + 1):
    if visited[i] == k:
        print(i)
        flag = True

if flag == False:
    print('-1')
