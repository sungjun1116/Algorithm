'''
data = list(map(int, input()))
length = len(data)

result1 = []
result2 = []

for i in range(length // 2):
    result1.append(data[i])

for i in range(length // 2, length):
    result2.append(data[i])

if sum(result1) == sum(result2):
    print("LUCKY")
else:
    print("READY")
'''

n = input()
length = len(n)  # 점수값의 총 자릿수
summary = 0

for i in range(length // 2):
    summary += int(n[i])

for i in range(length // 2):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")