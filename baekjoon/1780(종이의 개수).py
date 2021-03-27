import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
input = sys.stdin.readline

a, b, c = 0, 0, 0


def check(x, y, n):
    flag = True
    temp = arr[x][y]
    for i in range(x, x + n):
        if not flag:
            break
        for j in range(y, y + n):
            if arr[i][j] != temp:
                flag = False
                break
    if flag:
        return temp
    else:
        return "no"


def paper(x, y, n):
    global a, b, c
    result = check(x, y, n)
    if result == -1:
        a += 1
        return
    elif result == 0:
        b += 1
        return
    elif result == 1:
        c += 1
        return
    else:
        pass

    m = n // 3
    for i in range(x, x + (3 * m), m):
        for j in range(y, y + (3 * m), m):
            paper(i, j, m)
    return


paper(0, 0, n)
print(a)
print(b)
print(c)
