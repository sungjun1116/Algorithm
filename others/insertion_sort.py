def insertion_sort(arr):
    for index in range(1, len(arr)):
        temp = arr[index]
        prev = index - 1
        while prev >= 0 and arr[prev] > temp:
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = temp

    print(arr)
