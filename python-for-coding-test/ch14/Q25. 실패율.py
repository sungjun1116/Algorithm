def solution(N, stages):
    answer = []
    child = [0] * N  # 실패율의 분자
    parent = [0] * N  # 실패율의 분모

    for i in range(len(stages)):
        for j in range(N):
            if stages[i] >= j + 1:
                parent[j] += 1
            if stages[i] == j + 1:
                child[j] += 1

    # 실패율 리스트
    rate = []
    for i in range(N):
        result = (child[i] / parent[i]) if parent[i] != 0 else 0
        rate.append((result, i + 1))  # 리스트에 (실패율, 스테이지 번호) 삽입

    # 실패율을 기준으로 내림차순 정렬
    rate.sort(key=lambda x: -x[0])

    # 정렬된 스테이지 번호를 answer 리스트에 삽입
    for item in rate:
        answer.append(item[1])

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
