n = int(input())

data = [0]
for _ in range(n):
    data.append(int(input()))

dp = [0] * 10001
dp[1] = data[1]
dp[2] = data[1] + data[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 2] + data[i], dp[i - 3] + data[i - 1] + data[i])
    dp[i] = max(dp[i - 1], dp[i])  # 마지막 포도주를 무조건 안마셔도 되기 때문에 추가

print(dp[n])