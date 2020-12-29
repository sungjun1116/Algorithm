import heapq

n = int(input())

q = []
for i in range(n):
    heapq.heappush(q, int(input()))

result = 0
while len(q) > 1:  # while True, if len(q) == 1: break로 하면 안됨
    first = heapq.heappop(q)
    second = heapq.heappop(q)
    result += first + second
    heapq.heappush(q, first + second)

print(result)