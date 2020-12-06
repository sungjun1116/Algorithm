# 내 풀이
n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

array = []
for j in range(n):
    array.append(min(graph[j]))


print(max(array))

# 교재 풀이
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
# 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    result = max(min_value, result)

print(result)
