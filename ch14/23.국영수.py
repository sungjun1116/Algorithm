n = int(input())
array = []

for i in range(n):
    data = input().split()
    array.append((data[0], int(data[1]), int(data[2]), int(data[3])))


array.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for item in array:
    print(item[0])
