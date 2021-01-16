import itertools

n = int(input())
k = int(input())

data = []
for _ in range(n):
    data.append(input())

result = []
for x in itertools.permutations(data, k):
    answer = ''.join(list(x))
    result.append(answer)

result = set(result)
print(len(result))

