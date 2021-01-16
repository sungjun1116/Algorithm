n = int(input())

data = [0] * 10001
for i in range(1, n + 1):
    data[i] = int(input())


dp = [0] * 10001
dp[1] = data[1]
dp[2] = data[1] + data[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 2] + data[i], dp[i - 3] + data[i - 1] + data[i])
    dp[i] = max(dp[i - 1], dp[i])  # 포도주를 2번연속 안 먹을 경우가 존재하기 때문에 추가

print(dp[n])