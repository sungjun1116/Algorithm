import sys
from collections import Counter

input = sys.stdin.readline

def modefinder(numbers):
    c = Counter(numbers)
    order = c.most_common()
    maximum = order[0][1]

    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    if len(modes) > 1:
        return modes[1]
    else:
        return modes[0]


n = int(input())

array = [int(input()) for _ in range(n)]
array.sort()


print(int(round(sum(array) / len(array), 0)))
print(array[len(array) // 2])
print(modefinder(array))
print(max(array) - min(array))