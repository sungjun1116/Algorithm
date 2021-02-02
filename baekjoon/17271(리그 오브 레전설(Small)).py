import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dp = [0] * 10001

for i in range(1, m):
    dp[i] = 1
dp[m] = 2

for i in range(m + 1, n + 1):
    dp[i] = (dp[i - 1] + dp[i - m]) % 1000000007

print(dp[n])
