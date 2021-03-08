n = int(input())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))

def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [0]
for i in range(1, n + 1):
    parent.append(i)

# Union 연산을 각각 수행
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if arr[i][j] == 1:
            union_parent(parent, i + 1, j + 1)

for i in range(len(plan)):
    plan[i] = find_parent(parent, plan[i])

flag = True
temp = plan[0]
for i in range(1, len(plan)):
    if plan[i] == temp:
        continue
    else:
        flag = False

if flag is True:
    print("YES")
else:
    print("NO")
