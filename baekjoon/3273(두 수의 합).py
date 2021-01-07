n = int(input())
data = list(map(int, input().split()))
target = int(input())

data.sort()
left, right = 0, len(data) - 1

count = 0
while not left == right:
    # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
    if data[left] + data[right] < target:
        left += 1
    # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
    elif data[left] + data[right] > target:
        right -= 1
    else:
        count += 1
        left += 1



print(count)

