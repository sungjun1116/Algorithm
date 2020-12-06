g = int(input())
p = int(input())


def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 부모 테이블 초기하기
parent = [0] * (g + 1)
# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, g + 1):
    parent[i] = i

count = 0
for _ in range(p):
    data = int(input())
    parent_data = find_parent(parent, data)
    if parent_data == 0:
        break
    else:
        union_parent(parent, parent_data, parent_data- 1)
        count += 1


print(count)
