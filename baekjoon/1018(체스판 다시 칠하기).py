n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]


def check(x, y):
    cnt1 = 0
    for i in range(x, x + 8):
        for j in range(y, y + 8, 2):
            if i % 2 == 0:
                if arr[i][j] != 'W':
                    cnt1 += 1
                if arr[i][j + 1] != 'B':
                    cnt1 += 1
            else:
                if arr[i][j] != 'B':
                    cnt1 += 1
                if arr[i][j + 1] != 'W':
                    cnt1 += 1
    cnt2 = 0
    for i in range(x, x + 8):
        for j in range(y, y + 8, 2):
            if i % 2 == 0:
                if arr[i][j] != 'B':
                    cnt2 += 1
                if arr[i][j + 1] != 'W':
                    cnt2 += 1
            else:
                if arr[i][j] != 'W':
                    cnt2 += 1
                if arr[i][j + 1] != 'B':
                    cnt2 += 1
    return min(cnt1, cnt2)


result = int(1e9)
for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        result = min(result, check(i, j))

if result == int(1e9):
    print(0)
else:
    print(result)
