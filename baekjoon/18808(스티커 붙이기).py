import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
note = [[0] * m for i in range(n)]


def rotate(paper):
    r, c = len(paper), len(paper[0])
    return [[paper[r - 1 - j][i] for j in range(r)] for i in range(c)]


def pastable(x, y):
    for i in range(r):
        for j in range(c):
            if note[x + i][y + j] == 1 and paper[i][j] == 1:
                return False
    for i in range(r):
        for j in range(c):
            if paper[i][j] == 1:
                note[x + i][y + j] = 1

    return True


for _ in range(k):
    r, c = map(int, input().split())
    paper = [list(map(int, input().split())) for _ in range(r)]
    for rot in range(4):
        is_paste = False
        for x in range(n - r + 1):
            if is_paste:
                break
            for y in range(m - c + 1):
                if pastable(x, y):
                    is_paste = True
                    break
        if is_paste:
            break
        if rot != 3:
            paper = rotate(paper)
            r, c = c, r

print(sum([sum(L) for L in note]))
