# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        result = 0
        # 절단기 높이의 초기값을 mid 로 지정
        mid = (start + end) // 2
        # 절단기 높이가 mid 일경우 잘린 떡의 길이 구하기
        for item in array:
            if item >= mid:
                result += item - mid

        # 이진 탐색 원리를 이용해 최대 절단기의 높이 찾기
        if result == target:
            return mid
        elif result > target:
            start = mid + 1
        else:
            end = mid - 1
    return mid


# 요청한 떡의 개수 N과 요청한 떡의 길이 M을 입력받기
n, m = map(int, input().split())

data = list(map(int, input().split()))
print(binary_search(data, m, 0, max(data)))



