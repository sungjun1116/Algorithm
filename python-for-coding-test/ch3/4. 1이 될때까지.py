n, k = map(int, input().split())
result = 0
'''
while True:
    if n % k == 0:
       n = n // k
    else:
        n -= 1
    result += 1

    if n == 1:
        break

print(result)
'''
# 빠른 풀이
while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수없을 때) 반복문 탈출
    if n < k:
        break

    # K로 나누기
    n //= k
    result += 1
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)