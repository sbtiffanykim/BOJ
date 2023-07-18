n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
curr = [0] * m


def compute(k, st):
    if k == m:
        for i in range(m):
            print(curr[i], end=' ')
        print('')
        return

    temp = 0
    for i in range(st, n):
        if temp != nums[i]:
            curr[k] = nums[i]
            temp = curr[k]
            compute(k + 1, i)


compute(0, 0)
