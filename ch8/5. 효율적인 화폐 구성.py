"""
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0

for item in array:
    for i in range(item, m + 1):
        if d[i - item] != 10001:
            d[i] = min(d[i], d[i - item] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
"""


# 그리디 알고리즘 개념 적용(item이 큰 수일 수록 d[i - item]은 작아진다.)
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))
array.sort()

d = [10001] * (m + 1)
d[0] = 0

for item in array:
    for i in range(item, m + 1):
        if d[i - item] != 10001:
            d[i] = d[i - item] + 1

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
