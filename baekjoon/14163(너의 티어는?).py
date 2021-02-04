w, l, d = map(float, input().split())

dp = [[0] * 3001 for _ in range(21)]
dp[0][2000] = 1

for i in range(1, 21):
    for j in range(1000, 3001):
        if dp[i - 1][j] == 0:
            continue
        dp[i][j + 50] += dp[i - 1][j] * w
        dp[i][j - 50] += dp[i - 1][j] * l
        dp[i][j] += dp[i - 1][j] * d

a, b, c, d, e = 0.0, 0.0, 0.0, 0.0, 0.0
for i in range(1000, 3001):
    if 1000 <= i < 1500:
        a += dp[20][i]
    elif 1500 <= i < 2000:
        b += dp[20][i]
    elif 2000 <= i < 2500:
        c += dp[20][i]
    elif 2500 <= i < 3000:
        d += dp[20][i]
    else:
        e += dp[20][i]

print('%.8f' % a)
print('%.8f' % b)
print('%.8f' % c)
print('%.8f' % d)
print('%.8f' % e)

