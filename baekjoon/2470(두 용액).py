n = int(input())
data = sorted(list(map(int, input().split())))

left, right = 0, n - 1
answer = data[left] + data[right]
ans_left, ans_right = left, right

while left < right:
    temp = data[left] + data[right]
    if abs(temp) < abs(answer):
        answer = temp
        ans_left = left
        ans_right = right
        if abs(temp) < abs(answer) == 0:
            break
    if temp < 0:
        left += 1
    else:
        right -= 1


print(data[ans_left], data[ans_right])

