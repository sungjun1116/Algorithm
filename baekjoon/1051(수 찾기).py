import sys

input = sys.stdin.readline


# 가장 큰 정사각형의 한 변의 길이를 반환하는 함수
def max_square(n, m, size):
    while True:
        if size == 0:
            return 1
        for i in range(0, n - size):  # 세로로 이동
            for j in range(0, m - size):  # 가로로 이동
                if graph[i][j] == graph[i + size][j] == graph[i + size][j + size] == graph[i][j + size]:
                    return size + 1
        size -= 1


# 그래프 생성
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))

max_size = max_square(n, m, n - 1)
result = max_size * max_size
print(result)
