n = int(input())
result = []
for i in range(n):
    result.append(input().split(' ~ '))

start_h = 0
start_m = 0
for i in range(n):
    x = int(result[i][0].split(":")[0])
    y = int(result[i][0].split(":")[1])

    if x > start_h:
        start_h = x
        start_m = y
    elif x == start_h:
        if start_m < y:
            start_h = x
            start_m = y

if start_h < 10:
    start_h = '0' + str(start_h)
else:
    start_h = str(start_h)
if start_m < 10:
    start_m = '0' + str(start_m)
else:
    start_m = str(start_m)


end_h = 23
end_m = 59
for i in range(n):
    x = int(result[i][1].split(":")[0])
    y = int(result[i][1].split(":")[1])

    if x < end_h:
        end_h = x
        end_m = y
    elif x == end_h:
        if end_m > y:
            end_h = x
            end_m = y

if end_h < 10:
    end_h = '0' + str(end_h)
else:
    end_h = str(end_h)
if end_m < 10:
    end_m = '0' + str(end_m)
else:
    end_m = str(end_m)

if (int(start_h) - int(end_h)) > 0:
    print(-1)
elif (int(start_h) == int(end_h)) and (int(start_m) - int(end_m)) > 0:
    print(-1)
else:
    print(f'{start_h}:{start_m} ~ {end_h}:{end_m}')

