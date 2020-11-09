n = int(input())

array = list(map(int, input().split()))
array.sort()

# length = len(array)
# if length % 2 == 0:
#     med = (length // 2) - 1
# else:
#     med = length // 2
# print(array[med])

print(array[(n - 1) // 2])
