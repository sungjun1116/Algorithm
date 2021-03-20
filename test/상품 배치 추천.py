n = int(input())
room = []
for _ in range(n):
    room.append(list(input().strip()))

pos = [0 for _ in range(n + 1)]


def check(k, i, j):
    k += 1
    for a in range(k):
        for b in range(k):
            if i + a >= n or j + b >= n:
                return False
            if int(room[i + a][j + b]) == 0:
                return False

    return True


for k in range(n):
    for i in range(n):
        for j in range(n):
            if int(room[i][j]) == 1:
                if check(k, i, j):
                    pos[k + 1] += 1

print("total:", sum(pos))
for i in range(n + 1):
    if pos[i] != 0:
        print("size[" + str(i) + "]:", pos[i])
