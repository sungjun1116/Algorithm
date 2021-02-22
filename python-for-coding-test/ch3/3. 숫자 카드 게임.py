n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

print(max([min(L) for L in data]))