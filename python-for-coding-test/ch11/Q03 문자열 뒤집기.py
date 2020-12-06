data = list(map(int, input()))
cnt = 0
for i in range(1, len(data)):
    #  첫 번째 원소와 다르거나 바뀔때 cnt 증가
    #  첫번째 원소가 1이면 문자열 전체의 1의 덩어리는 0의 덩어리보다 항상 크거나 같다.
    #  첫번째 원소가 0이면 문자열 전체의 0의 덩어리는 1의 덩어리보다 항상 크거나 같다.
    #  따라서 첫번째 원소와 다른 덩어리를 바꾸는게 더 적은 횟수가 든다.
    if data[0] != data[i] and data[i] != data[i - 1]:
        cnt += 1

print(cnt)


