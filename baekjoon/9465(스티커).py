import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    dp = []
    n = int(input())

    for _ in range(2):
        dp.append(list(map(int, input().split())))

    dp[0][1] = dp[0][1] + dp[1][0]
    dp[1][1] = dp[1][1] + dp[0][0]
    for j in range(2, n):
        for i in range(2):
            if i == 0:
                dp[i][j] = dp[i][j] + max(dp[i + 1][j - 1], dp[i][j - 2], dp[i + 1][j - 2])
            else:
                dp[i][j] = dp[i][j] + max(dp[i - 1][j - 1], dp[i][j - 2], dp[i - 1][j - 2])

    result = max(dp[0][n - 1], dp[1][n - 1])
    print(result)



