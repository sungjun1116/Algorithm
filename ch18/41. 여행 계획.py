def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

#  그래프 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 그래프가 연결되어 있으면 union 연산 수행
for a in range(n):
    for b in range(n):
        if graph[a][b] == 1:
           union_parent(parent, a + 1, b + 1)



# 여행 계획 입력 받기
data = list(map(int,input().split()))
#  여행 계획에 속하는 연속된 여행지의 루트가 동일한지 확인
flag = 1
for i in range(m - 1):
    if find_parent(parent, data[i]) != find_parent(parent, data[i + 1]):
        flag = 0

print("yes" if flag == 1 else "no")