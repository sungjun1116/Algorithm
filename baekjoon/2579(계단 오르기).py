n = int(input())

array = [0]
for i in range(n):
    array.append(int(input()))

dp = [0] * (n + 1)
dp[1] = array[1]
dp[2] = dp[1] + array[2]

count = 2
for i in range(3, n + 1):
    if count == 2:
        dp[i] = dp[i - 2] + array[i]
        count = 0
    else:
        dp[i] = max(dp[i - 1], dp[i - 2] + array[i])
        if dp[i] == dp[i - 1]:
            count += 1

print(dp[n])
