from itertools import *

n, m = map(int, input().split())
data = [i for i in range(1, n + 1)]

result = list(permutations(data, m))
# n, m = 4, 2 => [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]

for i in range(len(result)):
    for j in range(len(result[i])):
        # result[i][j] = "("  1  ","  2  ")"
        if str(result[i][j]).isnumeric():
            print(result[i][j], end=' ')
    print()
