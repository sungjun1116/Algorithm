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
