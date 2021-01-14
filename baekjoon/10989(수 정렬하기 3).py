import sys
input = sys.stdin.readline

n = int(input())
array = [0] * 10001

for i in range(n):
    array[int(input())] += 1

for i in range(1, 10001):
    if array[i] != 0:
        for _ in range(array[i]):
            print(i)