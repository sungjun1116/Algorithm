import itertools

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

result = []
for x in itertools.combinations([i for i in range(n)], n // 2):
    data = list(x)
    sum_team = 0
    for y in itertools.combinations(data, 2):
        team = list(y)
        sum_team += graph[team[0]][team[1]] + graph[team[1]][team[0]]
    result.append(sum_team)

start, end = 0, len(result) - 1
answer = int(1e9)
while start < end:
    answer = min(answer, abs(result[start] - result[end]))
    start += 1
    end -= 1

print(answer)