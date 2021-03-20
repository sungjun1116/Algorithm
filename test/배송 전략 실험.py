n = int(input())
data = list(map(int, input()))

dp = [0] * 50
dp[0] = 1

if data[1] == 1:
    dp[1] = 1
else:
    dp[1] = 0

for i in range(2, n):
    if data[i] == 0:
        dp[i] = 0
    else:
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n - 1])
