def quick_sort(arr, left, right):
    if left >= right:
        return

    # 분할(Divide)
    pivot = partition(arr, left, right)

    # 피벗은 제외한 2개의 부~분 배열을 대상으로 순환 호출
    quick_sort(arr, left, pivot - 1)  # 정복(Conquer)
    quick_sort(arr, pivot + 1, right)  # 정복(Conquer)


def partition(arr, left, right):
    i, j = left, right

    while i < j:
        while arr[left] < arr[j]:
            j -= 1
        while i < j and arr[left] >= arr[i]:
            i += 1
        arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[i] = arr[i], arr[left]
    return i


arr = [6, 5, 4, 3, 2, 1]
quick_sort(arr, 0, len(arr) - 1)
print(arr)