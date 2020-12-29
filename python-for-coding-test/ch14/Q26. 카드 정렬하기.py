import heapq

n = int(input())

# 우선순위 큐에 카드 묶음을 모두 넣는다.
q = []
for i in range(n):
    heapq.heappush(q, int(input()))

result = 0
while len(q) > 1:  # while True, if len(q) == 1: break로 하면 안됨
    # 가장 작은 두개의 카드 묶음을 꺼낸다.
    first = heapq.heappop(q)
    second = heapq.heappop(q)

    # 꺼낸 두개의 묶음을 더해서 우선순위 큐에 다시 넣는다.
    result += first + second
    heapq.heappush(q, first + second)

print(result)