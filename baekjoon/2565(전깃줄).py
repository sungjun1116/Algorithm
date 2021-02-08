n = int(input())

array = []
for _ in range(n):
    a, b = map(int, input().split())
    array.append((a, b))

array.sort()

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if array[i][1] > array[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
