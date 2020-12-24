import math

m, n = map(int, input().split())
array = [True for i in range(n + 1)]  # 처음엔 모든 수가 소수(True)인 것으로 초기화
array[1] = False

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1):
    j = 2
    while i * j <= n:
        array[i * j] = False
        j += 1
# 모든 소수 출력
for i in range(m, n + 1):
    if array[i]:
        print(i)