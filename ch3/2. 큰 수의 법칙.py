n, m, k = map(int, input().split())

array = list(map(int, input().split()))
array.sort(reverse=True)
result = 0

while True:
    for _ in range(k):
        if m == 0:
            break
        result += array[0]
        m -= 1
    if m == 0:
        break
    result += array[1]
    m -= 1

print(result)
