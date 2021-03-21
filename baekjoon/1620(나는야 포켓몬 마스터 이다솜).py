import sys

input = sys.stdin.readline


n, m = map(int, input().split())
data = [0]
dic = dict()
for i in range(1, n + 1):
    x = input().rstrip()
    data.append(x)
    dic[x] = i

for _ in range(m):
    y = input().rstrip()
    if y.isnumeric():
        print(data[int(y)])
    else:
        print(dic[y])