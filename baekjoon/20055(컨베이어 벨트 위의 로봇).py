from collections import deque

n, k = map(int, input().split())
arr = deque(list(map(int, input().split())))
robot = deque([0] * n)

result = 1
while True:
    # 1.벨트가 한 칸 회전한다.
    arr.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    # 2.가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    for i in range(-2, -n - 1, -1):
        if robot[i] == 1 and robot[i + 1] == 0 and arr[i + 1 - n] > 0:
            robot[i] = 0
            robot[i + 1] = 1
            arr[i + 1 - n] -= 1
    robot[-1] = 0

    # 3.올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    if robot[0] == 0 and arr[0] > 0:
        robot[0] = 1
        arr[0] -= 1

    # 4.내구도가 0인 칸의 개수가 k개 이상이라면 종료.
    if arr.count(0) >= k:
        break
    result += 1

print(result)