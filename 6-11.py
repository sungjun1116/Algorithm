n = int(input())

array = []
for i in range(n):
    data = input().split()
    data[1] = int(data[1])
    array.append((data[0], data[1]))

array.sort(key=lambda x: x[1])

for item in array:
    print(item[0], end=' ')
