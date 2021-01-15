# 내 윗줄에 나와 겹치는 라인에 퀸이 있는가?
def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


# 한줄씩 재귀하며 DFS를 실행
def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i
            if adjacent(x):
                dfs(x + 1)


n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)
