s1 = input()
s2 = input()

length_1 = len(s1) + 1
length_2 = len(s2) + 1

dp = [[0] * length_2 for _ in range(length_1)]

for i in range(1, length_1):
    for j in range(1, length_2):
        # s1과 s2에 가장 최근에 추가된 글자가 서로 같을 때
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # 기존에 주어진 문자열로 만들 수 있던 최대 길이

print(dp[length_1 - 1][length_2 - 1])