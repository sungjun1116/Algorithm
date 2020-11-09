import collections

n = int(input())
data = []
result = 0

for i in range(n):
    data.append(int(input()))
data.sort()
data = collections.deque(data)

if n == 1:
    print(data[0])
else:
    while len(data) >= 2:
        pre_data = data.popleft()
        data[0] = data[0] + pre_data
        result += data[0]

    print(result)

# 카드를 합칠때마다 최소 카드 묶음 두개를 어떻게 아는가....
# 우선 순위 큐 배우고 다시풀기!