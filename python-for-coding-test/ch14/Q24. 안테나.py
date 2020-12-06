n = int(input())

data = list(map(int, input().split()))
data.sort()

index = (n - 1) // 2
print(data[index])
