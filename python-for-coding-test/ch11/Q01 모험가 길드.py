'''내 풀이
import collections
n = int(input())
array = list(map(int, input().split()))
array.sort(reverse=True)
array = collections.deque(array)

result = 0
result2 = 0
while True:
    temp = array[0]
    for i in range(temp):
        array.popleft()
        if not array:
            break
    result += 1
    if not array:
        break

print(result)
'''

n = int(input())
array = list(map(int, input().split()))
array.sort()

result = 0
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in array:
    count += 1
    if count >= i:
        result += 1
        count = 0