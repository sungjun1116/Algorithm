n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
data = [[0 for _ in range(m)] for _ in range(n)]
data[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    if arr[nx][ny] == 0 and data[nx][ny] == 0:
        data[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 가 없는 경우
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        # 뒤로 갈 수 있다면 이동하기
        if arr[nx][ny] == 0:
            x, y = nx, ny
            turn_time = 0
        # 뒤가 벽으로 막혀있는 경우
        else:
            break

print(count)