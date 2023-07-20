# Time Complexity: O(n^2)


def bubble_sort(arr):
    n = len(arr)
    for j in range(n - 1):
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


num = list(map(int, input().split()))
print(bubble_sort(num))
