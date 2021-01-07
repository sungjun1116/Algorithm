import sys
import heapq

input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    heapq.heappush(h, int(input()))

for _ in range(len(h)):
    print(heapq.heappop(h))