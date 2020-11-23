n, k = map(int, input().split())
result = 0
'''
while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1
# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1
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