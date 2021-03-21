import heapq
import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m = int(input())
    min_q, max_q = [], []
    visited = [False] * 1000001

    for i in range(m):
        a, b = input().split()
        if a == 'I':
            heapq.heappush(min_q, (int(b), i))
            heapq.heappush(max_q, (-int(b), i))
            visited[i] = True
        else:
            if b == '-1':
                while min_q and not visited[min_q[0][1]]:
                    heapq.heappop(min_q)
                if min_q:
                    visited[min_q[0][1]] = False
                    heapq.heappop(min_q)
            else:
                while max_q and not visited[max_q[0][1]]:
                    heapq.heappop(max_q)
                if max_q:
                    visited[max_q[0][1]] = False
                    heapq.heappop(max_q)

    while min_q and not visited[min_q[0][1]]:
        heapq.heappop(min_q)
    while max_q and not visited[max_q[0][1]]:
        heapq.heappop(max_q)

    if min_q and max_q:
        print(-max_q[0][0], min_q[0][0])
    else:
        print('EMPTY')