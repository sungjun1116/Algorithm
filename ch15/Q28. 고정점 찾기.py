'''내 틀린 풀이 -> 시간복잡도 NlogN
from bisect import *


n = int(input())
result = -1

array = list(map(int, input().split()))
for i in range(n):
    if bisect_left(array, array[i]) == array[i]:
        result = i

if result == -1:
    print('-1')
else:
    print(result)
'''


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return array[mid]
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
index = binary_search(array, 0, n - 1)
if result is None:
    print('-1')
else:
    print(index)


