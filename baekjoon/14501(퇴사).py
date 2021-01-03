n = int(input())
t = [0] * (n + 1)  # 상담을 완료하는데 걸리는 기간
p = [0] * (n + 1)  # 상담을 했을 때 받을 수 있는 금액
dp = [0] * (n + 1)

for i in range(1, n + 1):
    x, y = map(int, input().split())
    t[i] = x
    p[i] = y


max_value = 0
# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n, 0, -1):
    time = t[i] + i
    if time < n + 1:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
        print(i, max_value)
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value
        print(i, max_value)

print(max_value)




