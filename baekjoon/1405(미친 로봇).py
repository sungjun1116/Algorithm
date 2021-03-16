import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# 로봇 확률로 움직인다. 방문한곳을 또 방문하면 그 확률 다(해당 표본) 실패로 돌아감
# 원점에서 시작해서 확률은 1이다, 사방으로 갈때 필요한 확률을 곱해서 , 확률공간을 축소해나간다.
# 4**14 승으로 백트레킹까지 하면 충분

PC = list(map(int, input().split()))
N = PC[0]
PC = list(map(lambda x: x/100, PC[1:]))  # E W S N
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
check = dict()
Fail, Succ = 0, 0


def DFS(x: int, y: int, w: float, n: int):
    global Fail, Succ
    # ❌ 반드시 실패인지 먼저 체크
    # 최대한 작동한 경우, 이미 방문한곳이었던 경우, 계속 더 갈 수 있는 경우 확률공간 분배
    if (x, y) in check and check[(x, y)]:
        Fail += w
        return
    if n == N:
        Succ += w
        return

    check[(x, y)] = True
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        DFS(nx, ny, w*PC[k], n+1)
    check[(x, y)] = False


DFS(0, 0, 1, 0)
print("%0.9f" % Succ)