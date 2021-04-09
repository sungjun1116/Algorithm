def hanoi(num, start, end, other):
    global cnt

    if num == 0:
        return

    # n-1개의 원반들을 다른 기둥으로 옮기고
    hanoi(num - 1, start, other, end)
    # 맨 아래 원반을 목적지 기둥으로 옮기고
    result.append((start, end))
    cnt += 1
    # 다른 기둥에 옮겼던 원반들을 목적지로 옮기기
    hanoi(num - 1, other, end, start)


n = int(input())
result = []
cnt = 0

hanoi(n, 1, 3, 2)
print(cnt)
for i in result:
    print(*i)