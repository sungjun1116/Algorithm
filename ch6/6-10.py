n = int(input())

array = []
for i in range(n):
    x = int(input())
    array.append(x)


array.sort(reverse=True)

for i in array:
    print(i, end=' ')
