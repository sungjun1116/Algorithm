# 1. 투 포인터를 이용한 풀이
while True:
    data = input()
    if data == '0':
        break

    left, right = 0, len(data) - 1
    flag = True
    while left <= right:
        if data[left] == data[right]:
            left += 1
            right -= 1
        else:
            flag = False
            break

    if flag is True:
        print('yes')
    else:
        print('no')

# 2. 리스트 슬라이싱을 이용한 풀이
while True:
    data = input()
    if data == '0':
        break

    x = list(data)
    if x == x[::-1]:
        print('yes')
    else:
        print('no')