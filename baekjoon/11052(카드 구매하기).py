n = int(input())
cards = list(map(int, input().split()))

dp = [0] * 1000
dp[0] = cards[0]
dp[1] = max(cards[1], dp[0] + cards[0])

for i in range(2, n):
    dp[i] = cards[i]
    for j in range(i - 1, -1, -1):
        dp[i] = max(dp[i], dp[j] + cards[i - j - 1])

print(dp[n - 1])