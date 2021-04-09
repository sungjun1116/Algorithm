import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))

start, end = 0, max(data)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    total = sum(i - mid if i > mid else 0 for i in data)  # 이렇게 안하면 시간초과남..

    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
