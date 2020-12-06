def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2



n, x = map(int, input().split())
array = list(map(int, input().split()))

for i in range(len(array)):
    if array[i] > x:
        next = i
if next is None:
    next = len(array) - 1


if binary_search(array, x, 0, n - 1) is None:
    print(-1)
else:
    result = binary_search(array, array[next], 0, n - 1) - binary_search(array, x, 0, n - 1)
    print(result)


print(binary_search(array, array[next], 0, n - 1))
print(binary_search(array, x, 0, n - 1))