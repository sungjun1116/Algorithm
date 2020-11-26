n = int(input())
d = [0] * 1001

d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 4
d[5] = 5

for i in range(6, n + 1):
    while i % 2 == 0:
        i = i % 2
    while i % 3 == 0:
        i = i % 3
    while i % 5 == 0:
        i = i % 5

    if i == 2 or i ==3 or i ==5:
        d[i] = i
