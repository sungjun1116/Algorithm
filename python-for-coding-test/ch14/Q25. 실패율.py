def solution(N, stages):
    answer = []
    child = [0] * N
    parent = [0] * N
    for i in range(len(stages)):
        for j in range(N):
            if stages[i] >= j + 1:
                parent[j] += 1
            if stages[i] == j + 1:
                child[j] += 1

    rate = []
    for i in range(N):
        result = (child[i] / parent[i]) if parent[i] != 0 else 0
        rate.append((result, i + 1))
    print(rate)

    rate.sort(key=lambda x: (-x[0], x[1]))

    for item in rate:
        answer.append(item[1])

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
