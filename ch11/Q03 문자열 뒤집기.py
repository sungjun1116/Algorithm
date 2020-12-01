# data = list(map(int, input()))
#
# #  전부 1로 바꾸는 경우
# count_0 = 0
# for i in range(len(data) - 1):
#     if data[i] == 1:
#         continue
#     else:
#         #  연속된 숫자의 마지막 까지 가기
#         if data[i] == data[i + 1]:
#             data[i] = 1
#             continue
#         # 연속된 덩어리를 바꾸고 count 증가
#         count_0 += 1
# #  전부 0으로 바꾸는 경우
# count_1 = 0
# for i in range(len(data) - 1):
#     if data[i] == 0:
#         continue
#     else:
#         if data[i] == data[i + 1]:
#             data[i] = 0
#             continue
#         count_1 += 1
#
#
# print(min(count_0, count_1))

data = list(map(int, input()))
count_0 = 0
count_1 = 0

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음수에서 1로 바뀌는 경우
        if data[i + 1] == 1:
            count_0 += 1
        else:
            count_1 = 1

print(min(count_1, count_1))
