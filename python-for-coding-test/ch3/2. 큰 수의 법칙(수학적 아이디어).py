n, m, k = map(int, input().split())

array = list(map(int, input().split()))
array.sort(reverse=True)

# 가장 큰 수가 더해지는 횟수 계산
count = m // (k + 1) * k
count += m % (k + 1)

result = 0
result += count * array[0]  # 가장 큰 수 더하기
result += (m - count) * array[1]  # 두 번째로 큰 수 더하기

print(result)
