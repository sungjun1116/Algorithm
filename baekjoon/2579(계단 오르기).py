n = int(input())

data = [0]
for i in range(n):
    data.append(int(input()))

dp = [0] * (n + 1)
dp[1] = data[1]
dp[2] = data[1] + data[2]
dp[3] = data[1] + data[3]

for i in range(4, n + 1):
    dp[i] = max(dp[i - 2] + data[i], dp[i - 3] + data[i - 1] + data[i])

for i in range(1, n + 1):
    print(dp[i])
