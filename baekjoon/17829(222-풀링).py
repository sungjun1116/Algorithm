n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]


def pulling(x, y, n):
    if n == 2:
        result = []
        for i in range(x, x + n):
            for j in range(y, y + n):
                result.append(array[i][j])
        result.sort()
        return result[-2]

    m = n // 2
    answer = [pulling(x, y, m), pulling(x, y + m, m), pulling(x + m, y, m), pulling(x + m, y + m, m)]
    answer.sort()

    return answer[-2]


print(pulling(0, 0, n))

