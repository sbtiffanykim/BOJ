n, m = map(int, input().split())
arr1 = [int(t) for t in input().split()]
arr2 = [int(t) for t in input().split()]
res = [0] * (n + m)


# use the merge sort
def merge_sort(idx1, idx2):
    for i in range(n + m):
        if idx1 == n:
            res[i] = arr2[idx2]
            idx2 += 1
        elif idx2 == m:
            res[i] = arr1[idx1]
            idx1 += 1
        elif arr1[idx1] <= arr2[idx2]:
            res[i] = arr1[idx1]
            idx1 += 1
        else:
            res[i] = arr2[idx2]
            idx2 += 1
    return res


res = merge_sort(0, 0)
print(*res)
