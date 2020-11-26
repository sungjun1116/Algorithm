'''내풀이
from bisect import *

n, x = map(int, input().split())

array = list(map(int, input().split()))

value_left = bisect_left(array, x)
value_right = bisect_right(array, x)

result = value_right - value_left

if result == 0:
    print('-1')
else:
    print(result)
'''

'''내 풀이2
def find_left(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            while array[mid] == target:
                mid -= 1
            mid += 1
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return n

def find_right(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            while array[mid] == target:
                mid += 1
            mid -= 1
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return n

n, x = map(int, input().split())

array = list(map(int, input().split()))

value_left = find_left(array, x, 0, n - 1)
value_right = find_right(array, x, 0, n - 1)

result = value_right - value_left + 1

if result == 1:
    print('-1')
else:
    print(result)
'''


def count_by_value(array, x):
    n = len(array)
    a = first(array, x, 0, n - 1)
    if a is None:
        return 0
    b = last(array, x, 0, n - 1)
    return b - a + 1


def first(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
            return mid
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return None


def last(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n, x = map(int, input().split())

array = list(map(int, input().split()))
count = count_by_value(array, x)

if count == 0:
    print('-1')
else:
    print(count)
