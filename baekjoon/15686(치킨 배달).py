import itertools

n, m = map(int, input().split())
INF = int(1e9)


def chicken_distance(home, chickens):
    result = 0
    for i in home:
        x = i[0]
        y = i[1]
        distance = INF
        for chicken in chickens:
            a = chicken[0]
            b = chicken[1]
            temp = abs(x - a) + abs(y - b)
            distance = min(distance, temp)
        result += distance
    return result


array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

chickens = []
home = []
for i in range(n):
    for j in range(n):
        if array[i][j] == 2:
            chickens.append((i, j))
        if array[i][j] == 1:
            home.append((i, j))

answer = INF
min_answer = INF
for i in range(1, m + 1):
    for x in itertools.combinations(chickens, i):
        x = list(x)
        answer = min(answer, chicken_distance(home, x))
    min_answer = min(min_answer, answer)

print(min_answer)
