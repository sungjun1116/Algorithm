import itertools

n, s = map(int, input().split())
data = list(map(int, input().split()))

count = 0
for i in range(1, n + 1):
    for x in itertools.combinations(data, i):
        if sum(list(x)) == s:
            count += 1

print(count)