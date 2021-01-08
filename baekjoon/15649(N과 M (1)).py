from itertools import *

n, m = map(int, input().split())
data = [i for i in range(1, n + 1)]

for x in permutations(data, m):
    result = list(x)
    for i in result:
        print(i, end=' ')
    print()

