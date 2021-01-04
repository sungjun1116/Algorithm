import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(n):
    graph[i].append(list(map(int, input().split())))

while True:
    