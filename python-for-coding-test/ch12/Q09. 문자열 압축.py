def solution(s):
    length = len(s)
    answer = length
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, length // 2 + 1):
        result = ""
        prev = s[:step]  # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step)의 크기만큼 증가시키며 이전 문자열과 비교
        for i in range(step, length, step):
            # 이전 상태와 동일하다면 압축 횟수(step) 증가
            if prev == s[i:i + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                result += str(count) + prev if count >= 2 else prev
                prev = s[i:i + step]
                count = 1
        # 남아 있는 문자열에 대해 처리
        result += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(result))
    return answer


print(solution("aabbaccc"))