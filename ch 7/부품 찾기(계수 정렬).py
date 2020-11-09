# N(가게의 부품 개수)을 입력받기
n = int(input())
array = [0] * 100001
input_data = map(int, input().split())

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input_data:
    array[i] = 1

# M(손님이 확인 요청한 부품 개수)입력 받기
m = int(input())
req = list(map(int, input().split()))

for i in req:
    if array[i] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")



