n = int(input())
array = list(map(int, input().split()))

array.sort()

time = 0
result = 0
for i in array:
    time += i
    result += time

print(result)
