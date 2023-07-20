# Time Complexity: O(n^2)


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # list 마지막 - 1 까지만 반복
        min_idx = i  # 기준점
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:  # 기준점과 현재 값 비교
                min_idx = j  # 제일 작은 값 가진 index로 바꿈
        arr[min_idx], arr[i] = arr[i], arr[min_idx]  # swap

    return arr


num = list(map(int, input().split()))
print(selection_sort(num))
