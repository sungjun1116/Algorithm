n = int(input())

# dp 테이블 생성
dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

# 다이나믹 프로그래밍 진행
for i in range(n):
    for j in range(i + 1):
        #  왼쪽 위에서 오는 경우
        if j == 0:
            left_up = 0
        else:
            left_up = dp[i - 1][j - 1]

        # 오른쪽 위에서 오는 경우
        if j == i:
            right_up = 0
        else:
            right_up = dp[i - 1][j]

        # 점화식
        dp[i][j] = dp[i][j] + max(left_up, right_up)

# 마지막 행의 가장 큰 값 찾기
result = 0
for i in range(n):
    result = max(result, dp[n - 1][i])

print(result)
# print(max(dp[n - 1]))  정답 풀이 참u
