n = int(input())

data = [0] * 301
for i in range(1, n + 1):
    data[i] = int(input())

dp = [0] * 301
dp[1] = data[1]
dp[2] = data[1] + data[2]
for i in range(3, n + 1):
    dp[i] = max(dp[i - 2] + data[i], dp[i - 3] + data[i - 1] + data[i])

print(dp[n])
