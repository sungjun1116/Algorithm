def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return 1
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return 0


# n개의 정수를 입력받고 오름차순 정렬
n = int(input())
array = list(map(int, input().split()))
array.sort()

# array 안에 존재하는지 알아볼 m개의 정수를 입력받아 리스트로 만듬
m = int(input())
compare = list(map(int, input().split()))

for target in compare:
    print(binary_search(array, target, 0, n - 1))
