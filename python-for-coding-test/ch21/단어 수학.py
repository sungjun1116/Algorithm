n = int(input())

array = []
for i in range(n):
    array.append(list(input()))

array.sort(key=lambda x: len(x), reverse=True)

count = 0
number = 9

# 제일 큰 문자열의 맨 앞글자

while True:
    for i in range(n):
        if count == 0:
            data = array[0][0]
        for j in range(len(array[i])):
            if array[i][j] == data:
                array[i][j] = number
    if len(array[i]) - 1 >= len(array[i + 1]):
        data = array[i][1]
    number -= 1
    count += 1

result = 0
for i in range(n):
    result += int("".join(map(str, array[i])))
print(result)