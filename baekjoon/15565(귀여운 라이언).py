n, k = map(int, input().split())
array = list(map(int, input().split()))

answer = int(1e9)

left, right = 0, 0
cnt = 0
for i in range(n):
    while right < n and cnt < k:
        if array[right] == 1:
            cnt += 1
        right += 1
    if cnt == k:
        answer = min(answer, right - left)
        if array[left] == 1:
            cnt -= 1
        left += 1

print(answer if answer != int(1e9) else -1)
