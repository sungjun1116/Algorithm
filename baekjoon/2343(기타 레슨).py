n, m = map(int, input().split())
lesson = list(map(int, input().split()))
start, end = max(lesson), sum(lesson)

while start <= end:
    mid = (start + end) // 2

    cnt = 0
    play_time = 0
    for l in lesson:
        # play_time이 m보다 커지면 새로운 dvd 필요
        if play_time + l > mid:
            cnt += 1
            play_time = 0
        play_time += l

    cnt += 1 if play_time else 0

    if cnt <= m:
        end = mid - 1
    else:
        start = mid + 1
print(start)