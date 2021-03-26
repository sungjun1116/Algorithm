n = int(input())
cities = sorted(list(map(int, input().split())))
m = int(input())

start, end = 0, max(cities)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for city in cities:
        if city > mid:
            total += mid
        else:
            total += city
    # 총 예산이 충분한 경우 정수 상한액 줄이기
    if total > m:
        end = mid - 1
    # 총 예산이 부족한 경우 정수 상한액 늘리기
    else:
        result = mid
        start = mid + 1


print(result)