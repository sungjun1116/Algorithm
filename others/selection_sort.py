def selection_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        min_index = i  # 가장 작은 원소의 인덱
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[min_index], arr[i] = arr[i], arr[min_index]
    print(arr)


selection_sort([9, 8, 6, 3, 1])
