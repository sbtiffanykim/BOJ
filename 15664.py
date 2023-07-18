n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
isused = [False] * n
curr = [0] * m


def compute(k, idx):
    if k == m:
        for i in range(m):
            print(curr[i], end=' ')
        print('')
        return

    temp = 0
    for i in range(idx, n):
        if temp != nums[i]:
            curr[k] = nums[i]
            temp = curr[k]
            compute(k + 1, i + 1)


compute(0, 0)
