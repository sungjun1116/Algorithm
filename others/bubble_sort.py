def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(1, length - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    print(arr)


bubble_sort([9, 8, 6, 3, 1])
