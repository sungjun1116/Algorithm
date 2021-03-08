import sys
sys.setrecursionlimit(10**6)

n, r, c = map(int, input().split())


def z(x, y, n):
    if n == 1:
        if x == 0 and y == 0:
            return 0
        if x == 0 and y == 1:
            return 1
        if x == 1 and y == 0:
            return 2
        if x == 1 and y == 1:
            return 3
    else:  # 2, 3, 4 분면의 경우 1사분면으로 이동시켜서 생각!
        half = 2 ** (n - 1)
        if x < half and y < half:
            tmp = z(x, y, n - 1)
            return tmp
        if x < half <= y:
            tmp = z(x, y - half, n - 1)
            return half * half + tmp
        if x >= half > y:
            tmp = z(x - half, y, n - 1)
            return 2 * (half * half) + tmp
        if x >= half and y >= half:
            tmp = z(x - half, y - half, n - 1)
            return 3 * (half * half) + tmp


print(z(r, c, n))
