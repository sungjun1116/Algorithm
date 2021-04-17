data = list(input())
n = len(data)

for i in range(n // 2):
    data[i], data[n - 1 - i] = data[n - 1 - i], data[i]

print("".join(data))