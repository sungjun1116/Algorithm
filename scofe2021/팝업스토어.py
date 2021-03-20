m, n = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        if i == 0:
            dp[i][j] = dp[i][j-1] + dp[i][j]
            continue
        if j == 0:
            dp[i][j] = dp[i - 1][j] + dp[i][j]
            continue
        dp[i][j] = dp[i][j] + max(dp[i - 1][j], dp[i][j - 1])

print(dp[n - 1][m - 1])
